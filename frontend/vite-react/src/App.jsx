import React, { useState, useEffect } from 'react';
import { TopNavbar } from './components/TopNavbar';
import { Sidebar } from './components/Sidebar';
import { TodaysHighlights } from './components/TodaysHighlights';
import { PriceDrivers } from './components/PriceDrivers';
import { PriceForecastChart } from './components/PriceForecastChart';
import { fetchPriceForecast } from './services/api';
import styles from './App.module.css';

export default function App() {
  const [chartData, setChartData] = useState(null);

  useEffect(() => {
    async function loadData() {
      const data = await fetchPriceForecast('PL');
      if (data?.points) {
        setChartData(data.points);
      }
    }
    loadData();
  }, []);

  return (
    <div className={styles.layoutContainer}>
      <TopNavbar />
      <div className={styles.workspace}>
        <Sidebar />
        <main className={styles.mainGrid}>
          <div className={styles.topSection}>
            <TodaysHighlights />
            <PriceDrivers />
          </div>
          <div className={styles.bottomSection}>
            <PriceForecastChart data={chartData || undefined} />
          </div>
        </main>
      </div>
    </div>
  );
}