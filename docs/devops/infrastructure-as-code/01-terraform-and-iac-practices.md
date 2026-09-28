---
sidebar_position: 1
sidebar_label: "Terraform & IaC Practices"
description: "Terraform vs CloudFormation vs Pulumi, state and locking, modules and environments, drift, plan review, secrets and testing."
---

# Terraform & IaC Practices

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

---

## Q1. What is Infrastructure as Code and why does it matter?

**Short answer:** Infrastructure as Code means describing infrastructure — networks, clusters, databases, IAM — in version-controlled files and applying them with a tool, instead of clicking in a console. It gives you repeatable environments, code review for infrastructure changes, an audit trail, and the ability to rebuild after a disaster.

**How it works:** Most IaC tools are **declarative**: you describe the end state, and the tool computes the difference from the current state and makes the changes. The workflow mirrors application code: branch → PR with a plan → review → apply from a pipeline.

**Trade-offs and pitfalls:** IaC only helps if it's the *only* way changes happen. "Just this once" console fixes create drift and surprise at the next apply.

<details>
<summary>Follow-up questions</summary>

- Declarative vs imperative IaC — what's the difference?
- How do you bring existing hand-built infrastructure under IaC? (import)

</details>

**Remember:** Infrastructure changes should go through the same review and pipeline as code.

---

## Q2. Terraform vs CloudFormation vs Pulumi — how do you choose?

**Short answer:** Terraform (and its open-source fork OpenTofu) is a multi-cloud declarative tool using HCL with a large provider ecosystem. CloudFormation is AWS-native, with state managed by AWS; CDK lets you write it in TypeScript or Python. Pulumi uses general-purpose languages for multi-cloud IaC. I choose based on cloud footprint, team skills, and how much logic the infrastructure really needs.

| | Terraform / OpenTofu | CloudFormation (+ CDK) | Pulumi |
| --- | --- | --- | --- |
| Clouds | Many, plus SaaS providers (DNS, monitoring, GitHub) | AWS only | Many |
| Language | HCL (declarative) | YAML/JSON; CDK in TS/Python/Java/Go/C# | TS, Python, Go, C#, Java, YAML |
| State | You manage (remote backend) or a managed service | Managed by AWS (stacks) | Pulumi Cloud or self-managed backend |
| Strengths | Ecosystem, explicit plans, widely known | Deep AWS integration, rollbacks on failure | Real language features, testing, abstractions |
| Watch out for | State management, HCL limits for complex logic | AWS-only, slower support for some new features in the past | Too much cleverness makes infra hard to read |

**Example decision:** A mostly-AWS company that also manages Cloudflare DNS, Datadog monitors and GitHub repos picks Terraform for one consistent workflow. A small AWS-only team of TypeScript developers might pick CDK.

**Trade-offs and pitfalls:** Terraform's licence change (to the Business Source License) led to the OpenTofu fork; for most users both work similarly, but check your organisation's policy.

<details>
<summary>Follow-up questions</summary>

- When is a general-purpose language a benefit for IaC, and when is it a liability?
- How would you migrate from CloudFormation to Terraform?

</details>

**Remember:** Pick the tool that fits your cloud footprint and team; consistency matters more than the brand.

---

## Q3. What is Terraform state, and why do remote backends and locking matter?

**Short answer:** State is Terraform's record of which real resources correspond to which resources in your code, plus their attributes. Without it, Terraform can't compute a diff. In a team, state must live in a shared **remote backend** (for example S3, GCS, Azure Blob, or HCP Terraform) with **locking**, so two people can't apply at the same time and corrupt it. State often contains secrets, so it must be encrypted and access-controlled.

**Example:**

```hcl
terraform {
  required_version = ">= 1.6"

  backend "s3" {
    bucket       = "acme-terraform-state"       # versioned, encrypted bucket
    key          = "orders/prod/terraform.tfstate"
    region       = "eu-west-1"
    encrypt      = true
    use_lockfile = true   # S3-native locking (newer Terraform); older setups use a DynamoDB table
  }

  required_providers {
    aws = {
      source  = "hashicorp/aws"
      version = "~> 5.0"
    }
  }
}
```

**Trade-offs and pitfalls:**

- Local state files on laptops lead to lost or conflicting state.
- One giant state for everything means slow plans and a huge blast radius — split state by system and environment.
- Enable versioning on the state bucket so you can recover from corruption.
- Use `terraform state mv` / `moved` blocks when refactoring so resources aren't destroyed and recreated.

<details>
<summary>Follow-up questions</summary>

- Someone's apply crashed and left a stale lock. What do you do? (confirm no apply is running, then `force-unlock`)
- How do you share outputs between state files?

</details>

**Remember:** State maps code to reality — keep it remote, locked, encrypted and split sensibly.

---

## Q4. How do you structure modules and environments?

**Short answer:** Write reusable **modules** for common building blocks (a VPC, a service with its database and IAM), and compose them in thin per-environment root configurations that differ only by variables. Each environment gets its own state and usually its own cloud account or project.

**Example layout:**

```text
infra/
  modules/
    service/            # reusable: ECS/K8s service + IAM + alarms
      main.tf
      variables.tf
      outputs.tf
    network/
  envs/
    staging/
      main.tf           # calls modules with staging values
      backend.tf
    prod/
      main.tf
      backend.tf
```

```hcl
# envs/prod/main.tf
module "orders" {
  source = "../../modules/service"   # or a versioned registry/git source

  name           = "orders"
  environment    = "prod"
  instance_count = 6
  cpu            = 512
  memory         = 1024
  alarm_email    = "orders-oncall@example.com"
}
```

**Trade-offs and pitfalls:**

- Terraform workspaces are fine for identical copies, but separate directories (or tools like Terragrunt) make environment differences and permissions more explicit.
- Version shared modules (tags) so a module change doesn't silently hit every environment at once.
- Avoid "god modules" with dozens of flags — prefer composable smaller modules.

<details>
<summary>Follow-up questions</summary>

- Workspaces vs directories per environment — which do you prefer and why?
- How do you roll out a breaking change to a module used by 30 teams?

</details>

**Remember:** Reusable modules, thin environment roots, separate state per environment.

---

## Q5. What is drift and how do you detect and handle it?

**Short answer:** Drift is when real infrastructure no longer matches code — usually from manual console changes, other tools, or auto-scaling behaviour. Detect it by running scheduled `terraform plan` jobs (with `-detailed-exitcode`) and alerting on non-empty plans. Then either bring the code in line (if the manual change was right) or re-apply to revert it.

**Example:**

```bash
# Exit code 0 = no changes, 1 = error, 2 = changes (drift) present
terraform plan -detailed-exitcode -out=drift.plan
```

**Trade-offs and pitfalls:** Some attributes are legitimately changed outside Terraform (for example an autoscaler's desired count) — use `lifecycle { ignore_changes = [...] }` deliberately for those. Reduce drift at the source by limiting console write access in production.

<details>
<summary>Follow-up questions</summary>

- How would you handle an emergency console change made during an incident?

</details>

**Remember:** Detect drift on a schedule; fix it in code, not in the console.

---

## Q6. How should Terraform plans be reviewed and applied?

**Short answer:** Every change goes through a PR where CI runs `fmt`, `validate`, linting and policy checks, then posts the `plan` output for review. Reviewers pay special attention to destroys and replacements. After merge, a pipeline applies **the exact saved plan** using a narrowly-scoped identity — humans don't apply to production from laptops.

**How it works:**

```bash
terraform fmt -check
terraform validate
terraform plan -out=tfplan        # saved plan reviewed in the PR
terraform show -no-color tfplan   # human-readable, posted as a PR comment
terraform apply tfplan            # applies exactly what was reviewed
```

Things to look for in a plan:

- `-/+ destroy and then create replacement` on stateful resources (databases, volumes).
- Changes to IAM policies and security groups.
- Unexpectedly large change counts (often a provider upgrade or refactor gone wrong).

Tools: Atlantis, HCP Terraform, Spacelift, env0, or plain CI; policy-as-code with OPA/Conftest or Sentinel; static checks with tflint, Checkov or Trivy.

**Trade-offs and pitfalls:** Protect critical resources with `lifecycle { prevent_destroy = true }` and cloud-level deletion protection. A plan can go stale if someone applies another change first — re-plan before apply.

<details>
<summary>Follow-up questions</summary>

- A plan shows your production database will be replaced. What do you do?
- What policies would you enforce with policy-as-code?

</details>

**Remember:** Review the plan, apply the saved plan from a pipeline, and guard destructive changes.

---

## Q7. How do you handle secrets in IaC?

**Short answer:** Don't put secret values in `.tf` files or variable files in Git. Let the cloud generate and store secrets (for example managed database master passwords stored in a secret manager), reference secrets by ARN/ID from a secret manager, or inject them at apply time from the pipeline. Remember that values Terraform reads or creates may still end up in state, so treat state as sensitive.

**Example:**

```hcl
resource "aws_db_instance" "orders" {
  identifier                  = "orders-prod"
  engine                      = "postgres"
  instance_class              = "db.t4g.medium"   # illustrative size
  allocated_storage           = 50
  username                    = "orders_admin"
  manage_master_user_password = true   # RDS creates and stores the password in Secrets Manager
  deletion_protection         = true
  storage_encrypted           = true
}

variable "third_party_api_key" {
  type      = string
  sensitive = true   # hidden in plan output, but still stored in state
}
```

**Trade-offs and pitfalls:** `sensitive = true` only hides values from CLI output. Newer Terraform versions add ephemeral values and write-only arguments to avoid persisting some secrets in state — check your version.

<details>
<summary>Follow-up questions</summary>

- Who should be able to read state files?
- How do you rotate a secret that Terraform created?

</details>

**Remember:** Keep secrets out of code, generate them in the cloud, and treat state as secret.

---

## Q8. How do you test infrastructure code?

**Short answer:** Layer it like application testing: static checks (`fmt`, `validate`, tflint, security scanners) on every PR; policy checks on the plan; module tests (Terraform's native `terraform test`, or Terratest) that create real resources in a sandbox account and destroy them; and post-apply smoke tests.

**Trade-offs and pitfalls:** Real-resource tests are slow and cost money — run them for shared modules, not every root config. Mocked tests catch logic errors but not cloud API behaviour.

<details>
<summary>Follow-up questions</summary>

- What would you test in a shared VPC module?

</details>

**Remember:** Static checks always, policy on plans, real-resource tests for shared modules.

---

## Q9. How do you import existing resources and refactor safely?

**Short answer:** Use `import` blocks (or `terraform import`) to bring hand-built resources under management, then iterate until `plan` shows no changes. When renaming or moving resources between modules, use `moved` blocks so Terraform updates state instead of destroying and recreating.

**Example:**

```hcl
import {
  to = aws_s3_bucket.uploads
  id = "acme-prod-uploads"
}

moved {
  from = aws_s3_bucket.uploads
  to   = module.storage.aws_s3_bucket.uploads
}
```

**Remember:** Import until the plan is empty; `moved` blocks make refactors non-destructive.

---

## Q10. Where does IaC stop and GitOps or configuration management begin?

**Short answer:** A common split: Terraform provisions cloud infrastructure (networks, clusters, databases, IAM); GitOps tools (Argo CD, Flux) deploy and reconcile what runs *inside* Kubernetes; configuration management tools (Ansible and similar) handle VM-level configuration where VMs still exist. The boundary should be clear so two tools never manage the same resource.

**Trade-offs and pitfalls:** Managing Kubernetes app manifests through Terraform works but gives slower feedback and no continuous reconciliation. Crossplane lets Kubernetes manage cloud resources via CRDs — attractive for platform teams, but another control plane to run.

See [Platform Engineering & GitOps](../platform-engineering/01-platform-engineering-and-gitops.md).

**Remember:** One owner per resource: Terraform for cloud, GitOps for cluster workloads.

---

## References

- [Terraform documentation](https://developer.hashicorp.com/terraform/docs)
- [Terraform language: backends](https://developer.hashicorp.com/terraform/language/backend)
- [OpenTofu documentation](https://opentofu.org/docs/)
- [AWS CloudFormation documentation](https://docs.aws.amazon.com/cloudformation/)
- [AWS CDK documentation](https://docs.aws.amazon.com/cdk/)
- [Pulumi documentation](https://www.pulumi.com/docs/)
