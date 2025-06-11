import type {ReactNode} from 'react';
import clsx from 'clsx';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type FeatureItem = {
  title: string;
  Svg: React.ComponentType<React.ComponentProps<'svg'>>;
  description: ReactNode;
};

const FeatureList: FeatureItem[] = [
  {
    title: 'Coding Guidelines',
    Svg: require('@site/static/img/coding_guidelines.svg').default,
    description: (
      <>
        Develops and maintains coding guidelines focused on safety-critical
        applications in Rust.
      </>
    ),
  },
  {
    title: 'Tooling',
    Svg: require('@site/static/img/tooling.svg').default,
    description: (
      <>
        Aims to define and maintain a minimal, community-identified set of tools suggested for certifying Rust 
        in safety-critical applications. It maintains documentation on these tools and their development status, 
        helping guide adoption and compliance efforts.
      </>
    ),
  },
  {
    title: 'Liaison',
    Svg: require('@site/static/img/liaison.svg').default,
    description: (
      <>
        The liaison subcommittee will both proactively and reactively
        collaborate with other subcommittees in the consortium and outside
        groups such as standards committees, the Rust Project. The committee
        will work to drive agreement on various, potentially similar, safety
        critical efforts pertaining to Rust. The committee will also be the
        point of contact for any potential legal issues that may arise around IP
        as it pertains to references, upstreaming content and more.
      </>
    ),
  },
];

function Feature({title, Svg, description}: FeatureItem) {
  return (
    <div className={clsx('col col--4')}>
      <div className="text--center">
        <Svg className={styles.featureSvg} role="img" />
      </div>
      <div className="text--center padding-horiz--md">
        <Heading as="h3">{title}</Heading>
        <p>{description}</p>
      </div>
    </div>
  );
}

export default function HomepageFeatures(): ReactNode {
  return (
    <section className={styles.features}>
      <div className="container">
        <div className="row">
          {FeatureList.map((props, idx) => (
            <Feature key={idx} {...props} />
          ))}
        </div>
      </div>
    </section>
  );
}
