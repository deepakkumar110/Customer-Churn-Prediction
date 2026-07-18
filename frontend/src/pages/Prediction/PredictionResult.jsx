
function PredictionResult() {
  return (
    <div className="mt-8 bg-white border rounded-xl shadow-md p-6">

      <h2 className="text-2xl font-bold mb-4">
        Prediction Result
      </h2>

      <div className="flex items-center justify-between">

        <div>

          <p className="text-gray-600">
            Customer Status
          </p>

          <h3 className="text-2xl font-bold text-red-600">
            Churn
          </h3>

        </div>

        <div>

          <p className="text-gray-600">
            Confidence
          </p>

          <h3 className="text-2xl font-bold text-blue-600">
            92.45%
          </h3>

        </div>

      </div>

    </div>
  );
}

export default PredictionResult;