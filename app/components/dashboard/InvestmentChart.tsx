"use client";

import { Bar } from 'react-chartjs-2';
import {
  Chart as ChartJS,
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend,
} from 'chart.js';

ChartJS.register(
  CategoryScale,
  LinearScale,
  BarElement,
  Title,
  Tooltip,
  Legend
);

export default function InvestmentChart() {
  const options = {
    responsive: true,
    maintainAspectRatio: false,
    plugins: {
      legend: {
        position: 'top' as const,
      },
      title: {
        display: false,
      },
    },
  };
  
  const labels = ['서울', '경기', '인천', '부산', '대구', '광주', '대전'];
  
  const data = {
    labels,
    datasets: [
      {
        label: '3년 예상 수익률 (%)',
        data: [15.2, 18.7, 12.5, 9.8, 11.2, 10.5, 13.1],
        backgroundColor: 'rgba(99, 102, 241, 0.5)',
      },
      {
        label: '위험도',
        data: [7.8, 6.2, 5.9, 4.5, 6.1, 5.8, 6.5],
        backgroundColor: 'rgba(251, 113, 133, 0.5)',
      },
    ],
  };

  return <Bar options={options} data={data} />;
} 