import { Link, useLocation } from "react-router-dom";

function Sidebar() {
  const location = useLocation();

  return (
    <aside className="w-64 min-h-screen bg-white border-r border-gray-200 shadow-sm">

      <div className="p-6 border-b border-gray-200">
        <h2 className="text-2xl font-bold text-center text-blue-600">
          Churn AI
        </h2>
      </div>

      <nav className="p-5">

        <ul className="space-y-3">

          <li>
            <Link
              to="/"
              className={`block px-4 py-3 rounded-lg font-medium transition-all duration-200 ${
                location.pathname === "/"
                  ? "bg-blue-100 text-blue-700"
                  : "text-gray-700 hover:bg-gray-100"
              }`}
            >
              📊 Dashboard
            </Link>
          </li>

          <li>
            <Link
              to="/prediction"
              className={`block px-4 py-3 rounded-lg font-medium transition-all duration-200 ${
                location.pathname === "/prediction"
                  ? "bg-blue-100 text-blue-700"
                  : "text-gray-700 hover:bg-gray-100"
              }`}
            >
              🤖 Prediction
            </Link>
          </li>

        </ul>

      </nav>

    </aside>
  );
}

export default Sidebar;