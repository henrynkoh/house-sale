export default function Testimonials() {
  return (
    <section className="bg-white py-24 sm:py-32">
      <div className="mx-auto max-w-7xl px-6 lg:px-8">
        <div className="mx-auto max-w-2xl lg:text-center">
          <h2 className="text-base font-semibold leading-7 text-indigo-600">성공 사례</h2>
          <p className="mt-2 text-3xl font-bold tracking-tight text-gray-900 sm:text-4xl">
            100억 자산가의 비밀 전략
          </p>
          <p className="mt-6 text-lg leading-8 text-gray-600">
            AI 부동산 투자 전략을 실제로 적용해 성공한 투자자들의 이야기를 들어보세요.
          </p>
        </div>
        <div className="mx-auto mt-16 grid max-w-2xl grid-cols-1 gap-x-8 gap-y-20 lg:mx-0 lg:max-w-none lg:grid-cols-3">
          {testimonials.map((testimonial) => (
            <article key={testimonial.id} className="flex flex-col items-start justify-between p-6 bg-gray-50 rounded-2xl shadow-sm">
              <div className="relative">
                <p className="text-base italic font-medium text-gray-600">
                  "{testimonial.quote}"
                </p>
              </div>
              <div className="mt-8 flex items-center gap-x-4">
                <div className="h-10 w-10 rounded-full bg-gray-300" />
                <div className="text-sm leading-6">
                  <p className="font-semibold text-gray-900">{testimonial.name}</p>
                  <p className="text-gray-600">{testimonial.role}</p>
                </div>
              </div>
            </article>
          ))}
        </div>
      </div>
    </section>
  );
}

const testimonials = [
  {
    id: 1,
    quote: "AI 시스템의 추천으로 서울 외곽 지역에 투자했고, 2년 만에 40%의 수익률을 달성했습니다. 인간의 편향 없는 데이터 분석이 정말 놀랍습니다.",
    name: "김현우",
    role: "40대 사업가, 100억 자산가"
  },
  {
    id: 2,
    quote: "기존 부동산 중개사의 추천보다 AI 시스템의 분석이 훨씬 정확했습니다. 저평가된 지역을 발굴하고 선제적으로 투자할 수 있었습니다.",
    name: "이서연",
    role: "30대 투자자, 첫 투자 1년 만에 3억 수익"
  },
  {
    id: 3,
    quote: "처음에는 회의적이었지만, 시스템 추천 지역의 3년 후 가격 예측이 거의 정확했습니다. 이제는 모든 투자 결정에 AI를 활용합니다.",
    name: "박준호",
    role: "50대 자산관리사, 고객 포트폴리오 20% 수익률 달성"
  }
]; 