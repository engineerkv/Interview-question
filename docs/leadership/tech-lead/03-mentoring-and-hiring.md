---
sidebar_position: 3
sidebar_label: "Mentoring and Hiring"
description: "Mentoring junior and mid-level engineers, giving effective feedback, conducting technical interviews and designing interview rubrics."
---

# Mentoring, Feedback and Hiring

> **Reviewed:** 2026-09 · **Level:** Senior / Tech Lead · **Type:** Foundational

A Tech Lead multiplies the team's output by growing people and by hiring well. Interviewers look for concrete habits: how you mentor, how you give hard feedback, and how you make hiring decisions fair and consistent.

---

## Q1. How do you mentor a junior engineer?

**Short answer:** I start by understanding their goals and current strengths, then agree on a small number of growth areas. I give them well-scoped work slightly beyond their comfort zone, pair with them on the first steps, and gradually hand over ownership. I use regular one-to-ones, review their PRs with explanations rather than just fixes, and create opportunities for visibility such as demos. I check progress against the goals every few weeks.

**How to think about it:** Mentoring moves from *show* to *guide* to *support* to *delegate* as competence grows. Match the style to the person's level on each specific task.

**Example:** A junior engineer wants to get better at system design. Plan: shadow two design reviews, co-write a small design doc, then author one for a contained feature with the lead as reviewer.

**Trade-offs and pitfalls:** Over-helping creates dependency; under-supporting leads to failure and lost confidence. Mentoring only on technical skills misses communication and estimation, which often block promotion.

**Remember:** Goals, stretch work, scaffolding, gradual ownership, regular check-ins.

## Q2. How do you give difficult feedback?

**Short answer:** Privately, promptly and specifically. I describe the situation, the behavior and its impact, then ask for their perspective before suggesting a way forward, and agree on next steps. I focus on observable behavior, not personality, and follow up to recognize improvement.

**How to think about it:** The Situation-Behavior-Impact model keeps feedback factual. Feedback delayed until a performance review is unfair.

**Example:** "In yesterday's design review (situation), you interrupted Priya several times while she was presenting (behavior). She stopped contributing and we lost her input on the caching approach (impact). How did it feel from your side?"

**Trade-offs and pitfalls:** The "feedback sandwich" often hides the message. Avoid vague feedback ("be more senior") that cannot be acted on.

**Remember:** Private, prompt, specific, behavior and impact, then listen.

## Q3. A mid-level engineer wants to be promoted to senior. How do you help?

**Short answer:** I go through the career framework with them, identify the specific gaps with evidence, and create opportunities that close those gaps, such as leading a project, owning a cross-team design, or mentoring a newer engineer. We keep a record of their achievements and impact, and I advocate for them in calibration with concrete examples. I am honest about the timeline.

**How to think about it:** Promotion reflects already operating at the next level. The lead's job is to create the opportunities and make the evidence visible.

**Example:** Gap: influence beyond the team. Opportunity: lead the RFC for a shared component library with two other teams.

**Trade-offs and pitfalls:** Promising a promotion you do not control damages trust. Handing over only "glue work" without visible technical ownership can stall promotions.

**Remember:** Framework, gaps, opportunities, evidence, advocacy.

## Q4. How do you conduct a technical interview?

**Short answer:** I prepare with the role's rubric and a question that reflects real work, explain the format at the start, and make the candidate comfortable. I let them drive, give hints when stuck so I can see how they use them, and probe their reasoning and trade-offs. I take notes on evidence, not impressions, and write feedback against the rubric independently before discussing with other interviewers.

**How to think about it:** Interviews are measurement. Structure reduces noise and bias; a good candidate experience matters regardless of outcome.

**Example:** For a senior frontend role: a practical exercise such as building a debounced search with loading and error states, followed by discussion of accessibility, testing and scaling it to a design system component.

**Trade-offs and pitfalls:** Trivia and puzzle questions measure preparation rather than job ability. Discussing candidates before writing feedback causes anchoring.

**Remember:** Rubric, realistic problem, probe reasoning, evidence-based notes, independent write-up.

## Q5. How would you design an interview rubric?

**Short answer:** Start from the competencies the role actually needs, define observable signals for each at several levels, and make each interview stage own specific competencies so nothing is double-counted or missed. Calibrate interviewers with shadowing and reverse-shadowing, and review hiring outcomes periodically to refine the rubric.

**How to think about it:** A rubric turns "I liked them" into "they showed these specific signals".

**Example:**

| Competency | Below bar | At bar (Senior) | Above bar |
| --- | --- | --- | --- |
| Problem solving | Needs heavy guidance to structure the problem | Breaks problem down, considers edge cases unprompted | Identifies hidden requirements, compares multiple approaches |
| Code quality | Works but hard to follow, no tests considered | Readable, well-named, discusses testing | Designs for change, clear abstractions, strong test strategy |
| System design | Single-component view | Covers data flow, failure modes, scaling for stated load | Quantifies trade-offs, anticipates operational concerns |
| Communication | Hard to follow reasoning | Explains decisions clearly, responds to hints | Adapts to interviewer, drives the discussion |
| Collaboration and ownership | Blames others in examples | Concrete examples of ownership and teamwork | Examples of raising the bar for others |

**Trade-offs and pitfalls:** Over-detailed rubrics become checklists that miss the big picture. Rubrics that are never recalibrated drift.

**Remember:** Competencies, observable signals, stage ownership, calibration.

## Q6. How do you reduce bias in hiring?

**Short answer:** Structured interviews with the same core questions for each role, rubrics with observable signals, independent written feedback before debriefs, diverse interview panels, and interviewer training. In the debrief, I ask for evidence behind every rating and challenge vague terms like "culture fit", replacing them with defined values.

**How to think about it:** Bias thrives in unstructured judgment; structure and evidence reduce it.

**Example:** Replace "not a culture fit" with specific observations mapped to defined values such as "gave examples of collaborating across teams".

**Trade-offs and pitfalls:** Over-structuring can feel robotic; leave room for follow-up questions within the structure.

**Remember:** Structure, evidence, independence, diversity, training.

<details>
<summary>Follow-up questions</summary>

- What do you do when interviewers strongly disagree about a candidate? (Go back to the evidence per competency; if still split, consider an additional focused interview or default to the hiring bar policy.)
- How do you onboard a new senior hire quickly? (Onboarding buddy, a written 30/60/90-day plan, an early small win, and context documents like ADRs.)
- How do you mentor someone more experienced than you in some areas? (Mutual learning; focus on context, organization and goals rather than technical instruction.)

</details>

---

## References

- [StaffEng guides](https://staffeng.com/guides/)
- [Google Engineering Practices: How to write code review comments](https://google.github.io/eng-practices/review/reviewer/comments.html)
