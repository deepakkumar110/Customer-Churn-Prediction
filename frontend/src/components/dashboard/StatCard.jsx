
function StatCard({ title, value }) {
  return (
    <div className="bg-white rounded-xl shadow-md p-6 border">

      <h3 className="text-gray-500 text-sm font-medium">
        {title}
      </h3>

      <h2 className="text-3xl font-bold mt-2">
        {value}
      </h2>

    </div>
  );
}

export default StatCard;