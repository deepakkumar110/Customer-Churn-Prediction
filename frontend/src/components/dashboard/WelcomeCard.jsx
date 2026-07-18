function WelcomeCard() {
  return (
    <div className="bg-white rounded-xl shadow-lg p-6 border">

      <h1 className="text-3xl font-bold text-gray-800">
        Customer Churn Prediction Dashboard
      </h1>

      <p className="mt-3 text-gray-600">
        Welcome! This dashboard allows you to predict whether a customer is likely
        to churn based on customer information using our Machine Learning model.
      </p>

    </div>
  );
}

export default WelcomeCard;