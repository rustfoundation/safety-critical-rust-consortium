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
        TODO: fill in the description
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
        TODO: fill in the description
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
