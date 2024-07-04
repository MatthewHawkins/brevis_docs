/** @jsxImportSource @emotion/react */
import { css } from '@emotion/react'
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import useDocusaurusContext from '@docusaurus/useDocusaurusContext';
import Layout from '@theme/Layout';
import HomepageFeatures from '@site/src/components/HomepageFeatures';

import Heading from '@theme/Heading';
import styles from './index.module.css';
import FrontPageLink from '../components/widgets/FrontPageLink';

function HomepageHeader() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <header className={clsx('hero hero--primary', styles.heroBanner)}>
      <div className="container">
        <Heading as="h1" className="hero__title">
          {siteConfig.title}
        </Heading>
        <p className="hero__subtitle">{siteConfig.tagline}</p>
      </div>
    </header>
  );
}

export default function Home() {
  const {siteConfig} = useDocusaurusContext();
  return (
    <Layout
      title={`Hello from ${siteConfig.title}`}
      description="Description will go into a meta tag in <head />">
      <HomepageHeader />
      <main>
        {/* <HomepageFeatures /> */}
      </main>
      <div css={css`display:flex; flex-direction: row; gap: 20px; justify-self: center; width: 100%; justify-content: center; padding: 6rem 0;`}>
        <FrontPageLink imgPath={'https://docs.brevis.one/current/en/Content/Resources/Images/Images_EN/Kachel_ErsteSchritte.png'} description={"First Steps"} path={'/docs/category/first-steps'}/>
        <FrontPageLink imgPath={'https://docs.brevis.one/current/en/Content/Resources/Images/Images_EN/Kachel_QuickStart-Desktop.png'} description={"Desktop Edition - Quick Start Guide"} path={'/docs/installation/setting_up/first_steps/quick-start-guide'}/>
        <FrontPageLink imgPath={'https://docs.brevis.one/current/en/Content/Resources/Images/Images_EN/Kachel_QuickStart-Desktop.png'} description={"Desktop Extended Edition (DX1) - Quick Start Guide"} path={'/docs/installation/setting_up/first_steps/dx1'}/>
        <FrontPageLink imgPath={'https://docs.brevis.one/current/en/Content/Resources/Images/Images_EN/Kachel_QuickStart-Desktop.png'} description={"Rack Edition - Quick Start Guide"} path={'/docs/installation/setting_up/first_steps/rack-edition'}/>
        <FrontPageLink imgPath={'https://docs.brevis.one/current/en/Content/Resources/Images/Images_EN/Kachel_QuickStart-Desktop.png'} description={"Rack Extended Edition (RX2) - Quick Start Guide"} path={'/docs/installation/setting_up/first_steps/rx2'}/>
        <FrontPageLink imgPath={'https://docs.brevis.one/current/en/Content/Resources/Images/Images_EN/Kachel_ErsteSchritte.png'} description={"Outlook Plugin"} path={'/docs/category/outlook-plugin'}/>
      </div>
    </Layout>
  );
}
