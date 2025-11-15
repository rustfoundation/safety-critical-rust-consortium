import {themes as prismThemes} from 'prism-react-renderer';
import type {Config} from '@docusaurus/types';
import type * as Preset from '@docusaurus/preset-classic';

// This runs in Node.js - Don't use client-side code here (browser APIs, JSX...)

const baseUrl = process.env.BASE_URL || '/';

const config: Config = {
  title: 'Are We Safety Critical Yet?',
  tagline: 'It depends 🤔, we have a few certified compilers, a few certification products in-progress and a few use cases.',
  favicon: 'img/favicon.ico',

  // Set the production url of your site here
  url: 'https://your-docusaurus-site.example.com',
  // Set the /<baseUrl>/ pathname under which your site is served
  // For GitHub pages deployment, it is often '/<projectName>/'
  baseUrl: '/',

  // GitHub pages deployment config.
  // If you aren't using GitHub pages, you don't need these.
  organizationName: 'facebook', // Usually your GitHub org/user name.
  projectName: 'docusaurus', // Usually your repo name.

  onBrokenLinks: 'throw',
  onBrokenMarkdownLinks: 'warn',

  // Even if you don't use internationalization, you can use this field to set
  // useful metadata like html lang. For example, if your site is Chinese, you
  // may want to replace "en" with "zh-Hans".
  i18n: {
    defaultLocale: 'en',
    locales: ['en'],
  },

  presets: [
    [
      'classic',
      {
        docs: {
          path: 'docs/main',
          sidebarPath: './docs/sidebars.ts',
          // Please change this to your repo.
          // Remove this to remove the "edit this page" links.
          editUrl:
            'https://github.com/rustfoundation/safety-critical-rust-consortium/tree/main/arewesafetycriticalyet.org',
        },
        blog: false,
        theme: {
          customCss: './src/css/custom.css',
        },
      } satisfies Preset.Options,
    ],
  ],

  plugins: [
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'coding_guidelines',
        path: 'docs/coding_guidelines',
        routeBasePath: 'coding_guidelines',
        sidebarPath: './docs/sidebarsCodingGuidelines.ts',
        // ... other options
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'tooling',
        path: 'docs/tooling',
        routeBasePath: 'tooling',
        sidebarPath: './docs/sidebarsTooling.ts',
        // ... other options
      },
    ],
    [
      '@docusaurus/plugin-content-docs',
      {
        id: 'liaison',
        path: 'docs/liaison',
        routeBasePath: 'liaison',
        sidebarPath: './docs/sidebarsLiaison.ts',
        // ... other options
      },
    ],
    [
      '@docusaurus/plugin-client-redirects',
      {
        fromExtensions: ['html', 'htm'],
        redirects: [
          // /index.html -> /
          {
            to: '/index',
            from: '/',
          },
        ],
      },
    ]
  ],

  themeConfig: {
    // Replace with your project's social card
    image: 'img/docusaurus-social-card.jpg',
    navbar: {
      title: 'Are We Safety Critical Yet?',
      logo: {
        alt: 'The Safety Critical Rust Logo',
        src: 'img/rust_safety_logo.png',
      },
      items: [
        {
          type: 'docSidebar',
          docsPluginId: 'coding_guidelines',
          sidebarId: 'codingGuidelinesSidebar',
          position: 'left',
          label: 'Coding Guidelines',
        },
        {
          type: 'docSidebar',
          docsPluginId: 'tooling',
          sidebarId: 'toolingSidebar',
          position: 'left',
          label: 'Tooling',
        },
        {
          type: 'docSidebar',
          docsPluginId: 'liaison',
          sidebarId: 'liaisonSidebar',
          position: 'left',
          label: 'Liaison',
        },
        {
          href: 'https://github.com/rustfoundation/safety-critical-rust-consortium',
          label: 'GitHub',
          position: 'right',
        },
      ],
    },
    footer: {
      style: 'dark',
      links: [
        {
          title: 'Community',
          items: [
            {
              label: 'This site is powered through Netlify',
              href: 'https://netlify.com',
            },
          ],
        },
      ],
      copyright: `Copyright © ${new Date().getFullYear()} The Rust Safety Critical Working Group within the Rust Foundation.`,
    },
    prism: {
      theme: prismThemes.github,
      darkTheme: prismThemes.dracula,
    },
  } satisfies Preset.ThemeConfig,
};

export default config;
