import { 
  ChartBarIcon, 
  GlobeAltIcon, 
  HomeModernIcon, 
  CurrencyDollarIcon, 
  ArrowTrendingUpIcon 
} from '@heroicons/react/24/outline';

const features = [
  {
    name: '데이터 기반 분석',
    description: '부동산 등기정보 3.8억 건, 전세/월세 거래 이력 1.2억 건 등 방대한 데이터를 분석합니다.',
    icon: ChartBarIcon,
  },
  {
    name: '지역별 투자 추천',
    description: '전국 260개 시군구 중 투자 유망지역을 AI가 선별하여 추천해 드립니다.',
    icon: GlobeAltIcon,
  },
  {
    name: '실시간 시장 분석',
    description: '시간당 1,000만 건 이상의 데이터를 분석해 86.2%의 예측 정확도를 제공합니다.',
    icon: ArrowTrendingUpIcon,
  },
  {
    name: '맞춤형 투자 전략',
    description: '투자 목적, 자금, 기간에 따른 맞춤형 투자 전략을 수립해 드립니다.',
    icon: CurrencyDollarIcon,
  },
  {
    name: '부동산 포트폴리오 관리',
    description: '보유 부동산의 가치 평가, 수익률 분석, 매각 시점 예측 등을 제공합니다.',
    icon: HomeModernIcon,
  },
];

export default function Features() {
  return (
    <div className="bg-white py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl lg:text-center">
          <h2 className="text-base font-semibold leading-7 text-indigo-600">더 스마트한 투자</h2>
          <p className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            AI 부동산 투자의 핵심 메커니즘
          </p>
          <p className="mt-6 text-lg leading-8 text-gray-600">
            AI 기술을 활용해 부동산 투자에서 성공한 40대 CEO의 사례를 바탕으로 개발된 투자 시스템을 만나보세요.
          </p>
        </div>
        <div className="mx-auto mt-16 max-w-2xl sm:mt-20 lg:mt-24 lg:max-w-4xl">
          <dl className="grid max-w-xl grid-cols-1 gap-x-8 gap-y-10 lg:max-w-none lg:grid-cols-2 lg:gap-y-16">
            {features.map((feature) => (
              <div key={feature.name} className="relative pl-16">
                <dt className="text-base font-semibold leading-7 text-gray-900">
                  <div className="absolute left-0 top-0 flex h-10 w-10 items-center justify-center rounded-lg bg-indigo-600">
                    <feature.icon className="h-6 w-6 text-white" aria-hidden="true" />
                  </div>
                  {feature.name}
                </dt>
                <dd className="mt-2 text-base leading-7 text-gray-600">{feature.description}</dd>
              </div>
            ))}
          </dl>
        </div>
      </div>
    </div>
  );
} 