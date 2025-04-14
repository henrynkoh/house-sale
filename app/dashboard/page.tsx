import MainLayout from '../components/layout/MainLayout';
import StatsCard from '../components/dashboard/StatsCard';
import InvestmentChart from '../components/dashboard/InvestmentChart';
import PropertyMap from '../components/dashboard/PropertyMap';
import RecommendationList from '../components/dashboard/RecommendationList';

export default function Dashboard() {
  return (
    <MainLayout>
      <div className="py-10">
        <header>
          <div className="mx-auto max-w-7xl px-4 sm:px-6 lg:px-8">
            <h1 className="text-3xl font-bold leading-tight tracking-tight text-gray-900">투자 대시보드</h1>
          </div>
        </header>
        <main>
          <div className="mx-auto max-w-7xl sm:px-6 lg:px-8">
            {/* Dashboard stats */}
            <div className="px-4 py-8 sm:px-0">
              <div className="grid grid-cols-1 gap-5 sm:grid-cols-2 lg:grid-cols-4">
                <StatsCard 
                  title="최적 투자 지역" 
                  value="경기도 용인시" 
                  description="앞으로 3년간 35% 상승 예상" 
                  trend="up" 
                  trendValue="12.4%" 
                />
                <StatsCard 
                  title="유망 투자 상품" 
                  value="오피스텔" 
                  description="월 평균 임대 수익률" 
                  trend="up" 
                  trendValue="5.8%" 
                />
                <StatsCard 
                  title="시장 예측 정확도" 
                  value="86.2%" 
                  description="최근 12개월 기준" 
                  trend="up" 
                  trendValue="2.3%" 
                />
                <StatsCard 
                  title="평균 투자 수익률" 
                  value="22.5%" 
                  description="플랫폼 사용자 평균" 
                  trend="up" 
                  trendValue="8.7%" 
                />
              </div>
            </div>
            
            {/* Charts */}
            <div className="mt-8 px-4 sm:px-0">
              <div className="grid grid-cols-1 gap-5 lg:grid-cols-2">
                <div className="bg-white overflow-hidden shadow rounded-lg">
                  <div className="p-5">
                    <h3 className="text-lg leading-6 font-medium text-gray-900">
                      지역별 투자 수익률 예측
                    </h3>
                    <div className="mt-2 h-80">
                      <InvestmentChart />
                    </div>
                  </div>
                </div>
                <div className="bg-white overflow-hidden shadow rounded-lg">
                  <div className="p-5">
                    <h3 className="text-lg leading-6 font-medium text-gray-900">
                      투자 유망 지역 지도
                    </h3>
                    <div className="mt-2 h-80">
                      <PropertyMap />
                    </div>
                  </div>
                </div>
              </div>
            </div>
            
            {/* Recommendations */}
            <div className="mt-8 px-4 sm:px-0">
              <div className="bg-white overflow-hidden shadow rounded-lg">
                <div className="p-5">
                  <h3 className="text-lg leading-6 font-medium text-gray-900">
                    AI 추천 투자 물건
                  </h3>
                  <div className="mt-2">
                    <RecommendationList />
                  </div>
                </div>
              </div>
            </div>
          </div>
        </main>
      </div>
    </MainLayout>
  );
} 