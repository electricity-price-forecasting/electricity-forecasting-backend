const API_BASE_URL = process.env.REACT_APP_API_URL || 'http://localhost:8000/api/v1';

export const fetchPriceForecast = async (country = 'PL') => {
  try {
    const response = await fetch(`${API_BASE_URL}/forecast?country=${country}`);
    if (!response.ok) throw new Error(`HTTP Error: ${response.status}`);
    return await response.json();
  } catch (error) {
    console.warn('API error, falling back to mock dataset:', error);
    return null;
  }
};