export const SIDEBAR_MENU = [
  {
    category: 'MARKET',
    items: [
      { id: 'live', label: 'Live-prices', icon: '📡' },
      { id: 'ahead', label: 'Day-Ahead', icon: '📅' },
      { id: 'intraday', label: 'Intraday', icon: '🕒' },
      { id: 'forward', label: 'Forward Curve', icon: '📈' },
    ],
  },
  {
    category: 'ANALYSIS',
    items: [
      { id: 'p-drivers', label: 'Price Drivers', icon: '⚡' },
      { id: 'drivers', label: 'Drivers', icon: '🧩' },
      { id: 'forecasts', label: 'Forecasts', icon: '🔮' },
      { id: 'history', label: 'Prices History', icon: '📜' },
    ],
  },
  {
    category: 'TOOLS',
    items: [
      { id: 'alerts', label: 'Alerts', icon: '🔔' },
      { id: 'watchlist', label: 'Watchlist', icon: '✨' },
      { id: 'compare', label: 'Compare markets', icon: '⚖️' },
    ],
  },
];

export const DRIVERS_DATA = [
  { title: "Wind Generation", desc: "Strong downward pressure", val: "12 GW → 21 GW", tag: "-2.1%", type: "green", icon: "💨" },
  { title: "Solar Generation", desc: "Downward pressure", val: "12 GW → 21 GW", tag: "-2.1%", type: "green", icon: "☀️" },
  { title: "Electricity Demand", desc: "Moderate demand", val: "38 GW → 42 GW", tag: "+3€", type: "red", icon: "👥" },
  { title: "Gas Prices", desc: "High cost pressure", val: "+8%", tag: "+5€", type: "red", icon: "🔥" },
];

export const MOCK_CHART_DATA = [
  { time: '00:00 28 Jul', actual: 48, forecast: null, rangeHigh: 54 },
  { time: '04:00 28 Jul', actual: 62, forecast: null, rangeHigh: 70 },
  { time: '08:00 28 Jul', actual: 42, forecast: null, rangeHigh: 50 },
  { time: '12:00 28 Jul', actual: 68, forecast: null, rangeHigh: 76 },
  { time: '16:00 28 Jul', actual: 95, forecast: 95, rangeHigh: 110, isNow: true },
  { time: '18:00 28 Jul', actual: null, forecast: 90, rangeHigh: 105 },
  { time: '00:00 29 Jul', actual: null, forecast: 72, rangeHigh: 88 },
];