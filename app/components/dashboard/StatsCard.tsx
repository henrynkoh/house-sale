import { ArrowUpIcon, ArrowDownIcon } from '@heroicons/react/24/solid';

interface StatsCardProps {
  title: string;
  value: string;
  description: string;
  trend: 'up' | 'down' | 'neutral';
  trendValue: string;
}

export default function StatsCard({ title, value, description, trend, trendValue }: StatsCardProps) {
  return (
    <div className="bg-white overflow-hidden shadow rounded-lg">
      <div className="p-5">
        <div className="flex items-center">
          <div className="flex-shrink-0">
            <h3 className="text-sm font-medium text-gray-500 truncate">{title}</h3>
          </div>
        </div>
        <div className="mt-2">
          <p className="text-3xl font-semibold text-gray-900">{value}</p>
          <p className="mt-1 text-sm text-gray-500">{description}</p>
        </div>
        <div className="mt-4">
          <div className="flex items-center">
            {trend === 'up' ? (
              <ArrowUpIcon className="h-4 w-4 text-green-500" aria-hidden="true" />
            ) : trend === 'down' ? (
              <ArrowDownIcon className="h-4 w-4 text-red-500" aria-hidden="true" />
            ) : null}
            <span
              className={`ml-2 text-sm font-medium ${
                trend === 'up' ? 'text-green-500' : trend === 'down' ? 'text-red-500' : 'text-gray-500'
              }`}
            >
              {trendValue}
            </span>
          </div>
        </div>
      </div>
    </div>
  );
} 