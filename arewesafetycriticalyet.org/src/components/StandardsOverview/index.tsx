import type {ReactNode} from 'react';
import clsx from 'clsx';
import Link from '@docusaurus/Link';
import Heading from '@theme/Heading';
import styles from './styles.module.css';

type Rating = 'green' | 'yellow' | 'red' | 'grey';

interface Standard {
  name: string;
  rating: Rating;
  verdict: string;
  description: string;
  detailsUrl: string | null;
}

const standards: Standard[] = [
  {
    name: 'ISO 26262',
    rating: 'yellow',
    verdict: 'Achievable with moderate additional effort',
    description:
      "Rust's core language features - memory safety, strong typing, and data race prevention - provide an excellent basis for ISO 26262 compliance. Critical gaps exist in qualified tools, control/data flow analysis, and qualified RTOS/HAL/PAC support.",
    detailsUrl: '/docs/iso26262',
  },
  {
    name: 'IEC 61508',
    rating: 'grey',
    verdict: 'Analysis in preparation',
    description: 'Contributions welcome.',
    detailsUrl: null,
  },
  {
    name: 'DO-178C',
    rating: 'grey',
    verdict: 'Analysis in preparation',
    description: 'Contributions welcome.',
    detailsUrl: null,
  },
];

const ratingDotClass: Record<Rating, string> = {
  green: styles.dotGreen,
  yellow: styles.dotYellow,
  red: styles.dotRed,
  grey: styles.dotGrey,
};

const ratingCardClass: Record<Rating, string> = {
  green: styles.standardCardGreen,
  yellow: styles.standardCardYellow,
  red: styles.standardCardRed,
  grey: '',
};

function RatingDot({rating}: {rating: Rating}) {
  return <span className={clsx(styles.dot, ratingDotClass[rating])} />;
}

function StandardCard({standard}: {standard: Standard}) {
  return (
    <div
      className={clsx(
        styles.standardCard,
        ratingCardClass[standard.rating],
        !standard.detailsUrl && styles.standardCardPending,
      )}>
      <div className={styles.cardHeader}>
        <RatingDot rating={standard.rating} />
        <Heading as="h3">{standard.name}</Heading>
      </div>
      <p className={styles.verdict}>{standard.verdict}</p>
      <p className={styles.description}>{standard.description}</p>
      {standard.detailsUrl ? (
        <Link to={standard.detailsUrl} className={styles.detailsLink}>
          View detailed analysis &rarr;
        </Link>
      ) : (
        <Link
          to="https://github.com/rustfoundation/safety-critical-rust-consortium"
          className={styles.detailsLink}>
          Contribute on GitHub &rarr;
        </Link>
      )}
    </div>
  );
}

export default function StandardsOverview(): ReactNode {
  return (
    <section className={styles.overview}>
      <div className="container">
        <Heading as="h2" className="text--center margin-bottom--sm">
          Standards-Based Evaluations
        </Heading>
        <p className={clsx('text--center', styles.introText)}>
          Safety-critical readiness is measured by how well Rust's language design, toolchain, and
          ecosystem enable developers to meet the requirements of the relevant safety standards.
          For more context, see the{' '}
          <Link to="/docs/intro">full overview</Link>.
        </p>

        <div className={styles.legend}>
          <span className={styles.legendItem}>
            <RatingDot rating="green" /> Well supported
          </span>
          <span className={styles.legendItem}>
            <RatingDot rating="yellow" /> Achievable with effort
          </span>
          <span className={styles.legendItem}>
            <RatingDot rating="red" /> Gap
          </span>
          <span className={styles.legendItem}>
            <RatingDot rating="grey" /> Not yet rated
          </span>
        </div>

        <div className="row">
          {standards.map(standard => (
            <div className="col col--4 margin-bottom--lg" key={standard.name}>
              <StandardCard standard={standard} />
            </div>
          ))}
        </div>
      </div>
    </section>
  );
}
