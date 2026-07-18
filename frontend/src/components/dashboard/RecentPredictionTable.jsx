import StatusBadge from "../common/StatusBadge";

function RecentPredictionTable() {
  const data = [
    {
      id: 1,
      customer: "John Doe",
      prediction: "Churn",
      confidence: "92%",
    },
    {
      id: 2,
      customer: "Alice Smith",
      prediction: "Active",
      confidence: "95%",
    },
    {
      id: 3,
      customer: "Robert Brown",
      prediction: "Churn",
      confidence: "88%",
    },
    {
      id: 4,
      customer: "Emma Watson",
      prediction: "Active",
      confidence: "98%",
    },
  ];

  return (
    <div className="bg-white rounded-xl shadow-md border p-6">

      <h2 className="text-2xl font-bold mb-5">
        Recent Predictions
      </h2>

      <div className="overflow-x-auto">

        <table className="w-full">

          <thead>

            <tr className="border-b">

              <th className="text-left py-4">Customer</th>

              <th className="text-left py-4">Prediction</th>

              <th className="text-left py-4">Confidence</th>

            </tr>

          </thead>

          <tbody>

            {data.map((item) => (

              <tr
                key={item.id}
                className="border-b hover:bg-gray-50 transition"
              >

                <td className="py-4">
                  {item.customer}
                </td>

                <td className="py-4">
                  <StatusBadge status={item.prediction} />
                </td>

                <td className="py-4 font-semibold">
                  {item.confidence}
                </td>

              </tr>

            ))}

          </tbody>

        </table>

      </div>

    </div>
  );
}

export default RecentPredictionTable;