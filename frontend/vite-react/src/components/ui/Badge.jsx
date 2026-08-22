import React from 'react';
import styles from './Badge.module.css';

export const Badge = ({ children, type = 'green' }) => {
  return <span className={`${styles.badge} ${styles[type]}`}>{children}</span>;
};