import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Interview Prep Hub',
  tagline: 'Senior Engineer and Tech Lead interview preparation, from fundamentals to leadership',
  favicon: 'img/favicon.svg',

  future: {
    v4: true,
  },

  url: 'https://engineerkv.github.io',
  // GitHub Pages is a project site. Locally serve at http://localhost:3000
  baseUrl: process.env.GITHUB_ACTIONS === 'true' ? '/Interview-question/' : '/',
  organizationName: 'engineerkv',
  projectName: 'Interview-question',
  deploymentBranch: 'gh-pages',
  trailingSlash: false,

  onBrokenLinks: 'throw',
  onBrokenAnchors: 'warn',

  markdown: {
    format: 'detect',
    mermaid: true,
    hooks: {
      onBrokenMarkdownLinks: 'throw',
    },
  },

  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          routeBasePath: '/',
          sidebarPath: './sidebars.ts',
          editUrl: 'https://github.com/engineerkv/Interview-question/edit/main/',
          showLastUpdateTime: false,
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  themes: [
    '@docusaurus/theme-mermaid',
    [
      '@easyops-cn/docusaurus-search-local',
      {
        hashed: true,
        indexDocs: true,
        indexBlog: false,
        indexPages: false,
        docsRouteBasePath: '/',
        highlightSearchTermsOnTargetPage: true,
        searchResultLimits: 10,
        searchBarShortcutHint: true,
      },
    ],
  ],

  themeConfig: {
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: true,
    },
    docs: {
      sidebar: {
        hideable: true,
        autoCollapseCategories: true,
      },
    },
    tableOfContents: {
      minHeadingLevel: 2,
      maxHeadingLevel: 3,
    },
    navbar: {
      title: 'Interview Prep Hub',
      logo: {
        alt: 'Interview Prep Hub logo',
        src: 'img/logo.svg',
      },
      hideOnScroll: false,
      items: [
        {to: '/intro/learning-paths', label: 'Learning Paths', position: 'left'},
        {to: '/frontend', label: 'Frontend', position: 'left'},
        {to: '/case-studies', label: 'System Design', position: 'left'},
        {to: '/devops', label: 'DevOps', position: 'left'},
        {to: '/ai', label: 'AI', position: 'left'},
        {to: '/agentic-workflows', label: 'Agents', position: 'left'},
        {to: '/leadership', label: 'Tech Lead', position: 'left'},
        {to: '/reference', label: 'Cheatsheets', position: 'right'},
        {
          href: 'https://github.com/engineerkv/Interview-question',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Prepare',
          items: [
            {label: 'Learning paths', to: '/intro/learning-paths'},
            {label: 'Cheatsheets', to: '/reference'},
            {label: 'Case studies', to: '/case-studies'},
          ],
        },
        {
          title: 'Grow',
          items: [
            {label: 'Tech Lead', to: '/leadership'},
            {label: 'AI-assisted development', to: '/ai/ai-assisted-development'},
            {label: 'Agentic workflows', to: '/agentic-workflows'},
          ],
        },
        {
          title: 'Project',
          items: [
            {label: 'Content standards', to: '/contributing/content-standards'},
            {label: 'Repository assessment', to: '/intro/repository-assessment'},
            {label: 'GitHub', href: 'https://github.com/engineerkv/Interview-question'},
          ],
        },
      ],
      copyright: `Personal interview knowledge base. Built with Docusaurus.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
      additionalLanguages: ['bash', 'json', 'python', 'sql', 'yaml', 'docker', 'typescript'],
    },
    mermaid: {
      theme: {light: 'neutral', dark: 'dark'},
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
