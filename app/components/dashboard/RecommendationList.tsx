"use client";

import { useState } from 'react';
import { HomeModernIcon, BuildingOfficeIcon, BuildingStorefrontIcon } from '@heroicons/react/24/outline';

const recommendations = [
  {
    id: 1,
    name: '용인시 수지구 상현동 아파트',
    type: '아파트',
    price: '5억 8,000만원',
    expectedReturn: '35%',
    returnPeriod: '3년',
    confidenceScore: '92%',
    description: '신도시 개발 예정 지역 인근, 교통 개선 예정, 학군 우수',
    icon: HomeModernIcon,
  },
  {
    id: 2,
    name: '강남구 논현동 오피스텔',
    type: '오피스텔',
    price: '4억 2,000만원',
    expectedReturn: '28%',
    returnPeriod: '3년',
    confidenceScore: '89%',
    description: '역세권, 상권 발달, 임대 수요 높음',
    icon: BuildingOfficeIcon,
  },
  {
    id: 3,
    name: '송파구 문정동 상가',
    type: '상가',
    price: '7억 5,000만원',
    expectedReturn: '22%',
    returnPeriod: '5년',
    confidenceScore: '85%',
    description: '새로운 업무 단지 조성 중, 유동 인구 증가 예상',
    icon: BuildingStorefrontIcon,
  },
  {
    id: 4,
    name: '해운대구 우동 아파트',
    type: '아파트',
    price: '6억 3,000만원',
    expectedReturn: '24%',
    returnPeriod: '4년',
    confidenceScore: '87%',
    description: '관광지 인근, 재개발 계획, 해안가 프리미엄',
    icon: HomeModernIcon,
  },
];

export default function RecommendationList() {
  const [expanded, setExpanded] = useState<number | null>(null);

  const toggleExpand = (id: number) => {
    setExpanded(expanded === id ? null : id);
  };

  return (
    <div className="overflow-hidden">
      <ul className="divide-y divide-gray-200">
        {recommendations.map((property) => (
          <li key={property.id} className="py-4">
            <div className="flex items-center space-x-4">
              <div className="flex-shrink-0">
                <div className="flex items-center justify-center h-12 w-12 rounded-md bg-indigo-100 text-indigo-600">
                  <property.icon className="h-6 w-6" aria-hidden="true" />
                </div>
              </div>
              <div className="flex-1 min-w-0">
                <p className="text-sm font-medium text-gray-900 truncate">{property.name}</p>
                <div className="flex mt-1">
                  <span className="flex items-center text-sm text-gray-500">
                    <span className="truncate">예상 수익률: {property.expectedReturn}</span>
                    <span className="mx-2">•</span>
                    <span>신뢰도: {property.confidenceScore}</span>
                  </span>
                </div>
              </div>
              <div>
                <button
                  onClick={() => toggleExpand(property.id)}
                  className="inline-flex items-center px-3 py-1.5 border border-transparent text-xs font-medium rounded-full shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500"
                >
                  {expanded === property.id ? '접기' : '상세 정보'}
                </button>
              </div>
            </div>
            
            {expanded === property.id && (
              <div className="mt-4 ml-16 text-sm text-gray-700 bg-gray-50 p-4 rounded-md">
                <div className="grid grid-cols-2 gap-3">
                  <div>
                    <p className="text-gray-500">매매가</p>
                    <p className="font-medium">{property.price}</p>
                  </div>
                  <div>
                    <p className="text-gray-500">투자 기간</p>
                    <p className="font-medium">{property.returnPeriod}</p>
                  </div>
                  <div>
                    <p className="text-gray-500">매물 유형</p>
                    <p className="font-medium">{property.type}</p>
                  </div>
                  <div>
                    <p className="text-gray-500">예상 상승률</p>
                    <p className="font-medium">{property.expectedReturn}</p>
                  </div>
                </div>
                <div className="mt-3">
                  <p className="text-gray-500">AI 분석 코멘트</p>
                  <p className="mt-1">{property.description}</p>
                </div>
                <div className="mt-4">
                  <button className="inline-flex items-center px-3 py-2 border border-transparent text-sm leading-4 font-medium rounded-md shadow-sm text-white bg-indigo-600 hover:bg-indigo-700 focus:outline-none focus:ring-2 focus:ring-offset-2 focus:ring-indigo-500">
                    투자 시뮬레이션
                  </button>
                </div>
              </div>
            )}
          </li>
        ))}
      </ul>
    </div>
  );
} 