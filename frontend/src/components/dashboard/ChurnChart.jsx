
import {
  BarChart,
  Bar,
  XAxis,
  YAxis,
  CartesianGrid,
  Tooltip,
  ResponsiveContainer,
} from "recharts";

const data = [
  { month: "Jan", churn: 35 },
  { month: "Feb", churn: 28 },
  { month: "Mar", churn: 42 },
  { month: "Apr", churn: 31 },
  { month: "May", churn: 26 },
  { month: "Jun", churn: 39 },
];

function ChurnChart() {
  return (
    <div className="bg-white rounded-xl shadow-md border p-6">

      <h2 className="text-xl font-bold mb-6">
        Monthly Churn Analysis
      </h2>

      <div className="h-80">

        <ResponsiveContainer width="100%" height="100%">

          <BarChart data={data}>

            <CartesianGrid strokeDasharray="3 3" />

            <XAxis dataKey="month" />

            <YAxis />

            <Tooltip />

            <Bar
              dataKey="churn"
              fill="#2563eb"
              radius={[8, 8, 0, 0]}
            />

          </BarChart>

        </ResponsiveContainer>

      </div>

    </div>
  );
}

export default ChurnChart;