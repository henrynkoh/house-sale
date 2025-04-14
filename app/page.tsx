import MainLayout from './components/layout/MainLayout';
import Hero from './components/layout/Hero';
import Features from './components/layout/Features';
import Testimonials from './components/layout/Testimonials';
import CTA from './components/layout/CTA';

export default function Home() {
  return (
    <MainLayout>
      <Hero />
      <Features />
      <Testimonials />
      <CTA />
    </MainLayout>
  );
}
