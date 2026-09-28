import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

const config: Config = {
  title: 'Roundbook',
  tagline: 'Spoken answers for Senior Engineer and Tech Lead rounds',
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

  headTags: [
    {
      tagName: 'link',
      attributes: {
        rel: 'preconnect',
        href: 'https://fonts.googleapis.com',
      },
    },
    {
      tagName: 'link',
      attributes: {
        rel: 'preconnect',
        href: 'https://fonts.gstatic.com',
        crossorigin: 'anonymous',
      },
    },
  ],

  clientModules: ['./src/client/route-motion.ts'],

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
    metadata: [
      {
        name: 'description',
        content:
          'Roundbook is a quiet study book for Senior Engineer and Tech Lead interviews: spoken answers, design rounds, and pocket cards.',
      },
    ],
    colorMode: {
      defaultMode: 'light',
      respectPrefersColorScheme: false,
      disableSwitch: false,
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
      title: 'Roundbook',
      logo: {
        alt: 'Roundbook',
        src: 'img/logo.svg',
      },
      hideOnScroll: true,
      items: [
        {to: '/intro/learning-paths', label: 'Paths', position: 'left'},
        {
          type: 'dropdown',
          label: 'Library',
          position: 'left',
          items: [
            {to: '/frontend', label: 'Interface Engineering'},
            {to: '/backend/python', label: 'Service Engineering'},
            {to: '/case-studies', label: 'Design Rounds'},
            {to: '/devops', label: 'Production Engineering'},
            {to: '/ai', label: 'Applied AI'},
            {to: '/agentic-workflows', label: 'Agent Systems'},
            {to: '/leadership', label: 'Staff Craft'},
          ],
        },
        {to: '/reference', label: 'Pocket Cards', position: 'right'},
        {
          href: 'https://github.com/engineerkv/Interview-question',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'light',
      links: [
        {
          title: 'Study',
          items: [
            {label: 'Paths', to: '/intro/learning-paths'},
            {label: 'Pocket Cards', to: '/reference'},
            {label: 'Design Rounds', to: '/case-studies'},
          ],
        },
        {
          title: 'Craft',
          items: [
            {label: 'Staff Craft', to: '/leadership'},
            {label: 'Applied AI', to: '/ai'},
            {label: 'Agent Systems', to: '/agentic-workflows'},
          ],
        },
        {
          title: 'The book',
          items: [
            {label: 'House Style', to: '/contributing/content-standards'},
            {label: 'How to use Roundbook', to: '/intro'},
            {label: 'GitHub', href: 'https://github.com/engineerkv/Interview-question'},
          ],
        },
      ],
      copyright: `Roundbook · personal study notes for Senior Engineer and Tech Lead rounds.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.nightOwl,
      additionalLanguages: ['bash', 'json', 'python', 'sql', 'yaml', 'docker', 'typescript'],
    },
    mermaid: {
      theme: {light: 'neutral', dark: 'forest'},
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
