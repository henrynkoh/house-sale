"use client";

import { useEffect, useState } from 'react';

export default function PropertyMap() {
  const [loading, setLoading] = useState(true);

  useEffect(() => {
    // Simulate map loading delay
    const timer = setTimeout(() => {
      setLoading(false);
    }, 1000);
    
    return () => clearTimeout(timer);
  }, []);

  if (loading) {
    return (
      <div className="flex items-center justify-center h-full">
        <div className="animate-spin rounded-full h-10 w-10 border-b-2 border-indigo-500"></div>
      </div>
    );
  }

  return (
    <div className="h-full bg-gray-100 rounded">
      <div className="flex items-center justify-center h-full">
        <div className="text-center p-6">
          <div className="text-indigo-600 font-medium mb-2">투자 유망 지역 지도</div>
          <p className="text-gray-500 text-sm mb-4">
            실제 구현 시에는 Kakao Map, Naver Map 등의 API를 활용하여 
            투자 유망 지역을 시각화할 수 있습니다.
          </p>
          <div className="grid grid-cols-2 gap-2 text-xs text-left">
            <div className="bg-green-100 p-2 rounded">
              <div className="font-medium">경기도 용인시</div>
              <div className="text-gray-600">예상 수익률: 35%</div>
            </div>
            <div className="bg-green-100 p-2 rounded">
              <div className="font-medium">서울시 강남구</div>
              <div className="text-gray-600">예상 수익률: 28%</div>
            </div>
            <div className="bg-green-100 p-2 rounded">
              <div className="font-medium">부산시 해운대구</div>
              <div className="text-gray-600">예상 수익률: 23%</div>
            </div>
            <div className="bg-green-100 p-2 rounded">
              <div className="font-medium">인천시 송도동</div>
              <div className="text-gray-600">예상 수익률: 20%</div>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
} 