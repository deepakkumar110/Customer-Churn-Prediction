import { useState } from "react";
import MainLayout from "../../layouts/MainLayout";
import api from "../../api/predictionApi";

function Prediction() {
  const [formData, setFormData] = useState({
    gender: 1,
    SeniorCitizen: 0,
    Partner: 0,
    Dependents: 0,
    tenure: "",
    MonthlyCharges: "",
    TotalCharges: "",
    Contract: 0,
  });

  const [result, setResult] = useState(null);
  const [loading, setLoading] = useState(false);

  const handleChange = (e) => {
    const { name, value } = e.target;

    setFormData({
      ...formData,
      [name]: Number(value),
    });
  };

  const handleSubmit = async (e) => {
    e.preventDefault();

    setLoading(true);

    try {
      const response = await api.post("/predict", formData);
      setResult(response.data);
    } catch (error) {
      alert("Prediction Failed");
      console.log(error);
    }

    setLoading(false);
  };

  return (
    <MainLayout>
      <div className="bg-white rounded-xl shadow-md border p-8">

        <h1 className="text-3xl font-bold">
          Customer Churn Prediction
        </h1>

        <p className="text-gray-500 mt-2">
          Fill customer details below.
        </p>

        {/* Instructions */}

        <div className="mt-6 bg-blue-50 border border-blue-200 rounded-lg p-5">
          <h3 className="font-semibold text-blue-700 text-lg">
            Instructions
          </h3>

          <p className="text-gray-600 mt-2">
            Enter the customer's information carefully.
            The Machine Learning model will analyze these values
            and predict whether the customer is likely to churn.
          </p>
        </div>

        <form
          onSubmit={handleSubmit}
          className="grid grid-cols-1 md:grid-cols-2 gap-6 mt-8"
        >

          {/* Gender */}

          <div>
            <label className="font-semibold">
              Gender
            </label>

            <p className="text-sm text-gray-500 mb-2">
              Select customer's gender.
            </p>

            <select
              name="gender"
              onChange={handleChange}
              className="w-full border rounded-lg p-3"
            >
              <option value="1">Male</option>
              <option value="0">Female</option>
            </select>
          </div>

          {/* Senior Citizen */}

          <div>
            <label className="font-semibold">
              Senior Citizen
            </label>

            <p className="text-sm text-gray-500 mb-2">
              Is the customer 65 years or older?
            </p>

            <select
              name="SeniorCitizen"
              onChange={handleChange}
              className="w-full border rounded-lg p-3"
            >
              <option value="0">No</option>
              <option value="1">Yes</option>
            </select>
          </div>

          {/* Partner */}

          <div>
            <label className="font-semibold">
              Partner
            </label>

            <p className="text-sm text-gray-500 mb-2">
              Is the customer married or living with a partner?
            </p>

            <select
              name="Partner"
              onChange={handleChange}
              className="w-full border rounded-lg p-3"
            >
              <option value="0">No</option>
              <option value="1">Yes</option>
            </select>
          </div>

          {/* Dependents */}

          <div>
            <label className="font-semibold">
              Dependents
            </label>

            <p className="text-sm text-gray-500 mb-2">
              Does the customer have children or dependents?
            </p>

            <select
              name="Dependents"
              onChange={handleChange}
              className="w-full border rounded-lg p-3"
            >
              <option value="0">No</option>
              <option value="1">Yes</option>
            </select>
          </div>

          {/* Tenure */}

          <div>
            <label className="font-semibold">
              Tenure (Months)
            </label>

            <p className="text-sm text-gray-500 mb-2">
              Number of months the customer has stayed with the company.
            </p>

            <input
              type="number"
              name="tenure"
              placeholder="Example : 24"
              onChange={handleChange}
              className="w-full border rounded-lg p-3"
            />
          </div>

          {/* Monthly Charges */}

          <div>
            <label className="font-semibold">
              Monthly Charges ($)
            </label>

            <p className="text-sm text-gray-500 mb-2">
              Current monthly subscription amount.
            </p>

            <input
              type="number"
              name="MonthlyCharges"
              placeholder="Example : 79.99"
              onChange={handleChange}
              className="w-full border rounded-lg p-3"
            />
          </div>

          {/* Total Charges */}

          <div>
            <label className="font-semibold">
              Total Charges ($)
            </label>

            <p className="text-sm text-gray-500 mb-2">
              Total amount paid by the customer so far.
            </p>

            <input
              type="number"
              name="TotalCharges"
              placeholder="Example : 1899.50"
              onChange={handleChange}
              className="w-full border rounded-lg p-3"
            />
          </div>

          {/* Contract */}

          <div>
            <label className="font-semibold">
              Contract Type
            </label>

            <p className="text-sm text-gray-500 mb-2">
              Select the customer's subscription contract.
            </p>

            <select
              name="Contract"
              onChange={handleChange}
              className="w-full border rounded-lg p-3"
            >
              <option value="0">Month-to-month</option>
              <option value="1">One Year</option>
              <option value="2">Two Year</option>
            </select>
          </div>

          {/* Button */}

          <div className="md:col-span-2">
            <button
              type="submit"
              className="w-full bg-blue-600 text-white py-3 rounded-lg hover:bg-blue-700 transition"
            >
              {loading ? "Predicting..." : "Predict Customer Churn"}
            </button>
          </div>

        </form>

        {/* Result */}

        {result && (

          <div className="mt-8 border rounded-xl p-6 bg-gray-50">

            <h2 className="text-2xl font-bold mb-4">
              Prediction Result
            </h2>

            <p className="text-lg">
              <strong>Prediction :</strong> {result.prediction}
            </p>

            <p className="mt-2 text-lg">
              <strong>Confidence :</strong> {result.confidence}%
            </p>

            <div className="mt-5">

              {result.prediction === "Stay" ? (

                <div className="bg-green-100 text-green-700 rounded-lg p-4">
                  ✔ Lower Churn Risk
                </div>

              ) : (

                <div className="bg-red-100 text-red-700 rounded-lg p-4">
                  ⚠ High Churn Risk
                </div>

              )}

            </div>

          </div>

        )}

      </div>
    </MainLayout>
  );
}

export default Prediction;