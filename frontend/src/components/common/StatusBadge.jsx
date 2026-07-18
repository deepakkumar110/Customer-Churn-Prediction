
function StatusBadge({ status }) {
  const isChurn = status === "Churn";

  return (
    <span
      className={`px-3 py-1 rounded-full text-sm font-semibold ${
        isChurn
          ? "bg-red-100 text-red-600"
          : "bg-green-100 text-green-600"
      }`}
    >
      {status}
    </span>
  );
}

export default StatusBadge;