import MainLayout from "../../layouts/MainLayout";
import WelcomeCard from "../../components/dashboard/WelcomeCard";
import StatCard from "../../components/dashboard/StatCard";
import RecentPredictionTable from "../../components/dashboard/RecentPredictionTable";
import ChurnChart from "../../components/dashboard/ChurnChart";

function Dashboard() {
  return (
    <MainLayout>
      <div className="space-y-6">

        <WelcomeCard />

        <div className="grid grid-cols-1 md:grid-cols-2 lg:grid-cols-4 gap-6">

          <StatCard title="Total Customers" value="7043" />
          <StatCard title="Churn Rate" value="26.5%" />
          <StatCard title="Active Customers" value="5174" />
          <StatCard title="Predictions" value="128" />

        </div>

        <div className="grid grid-cols-1 lg:grid-cols-2 gap-6">

          <ChurnChart />

          <RecentPredictionTable />

        </div>

      </div>
    </MainLayout>
  );
}

export default Dashboard;