import Image from "next/image";
import logo from "/public/logo.png";
import { FaPaperPlane, FaRobot } from "react-icons/fa"; // Import an icon from React Icons

export default function Page() {
  return (
    <div className="container">
      <div className="flex flex-col md:flex-row ">
        {/* Sidebar */}
        <div className="w-64 h-screen bg-gray-800">
          <div className="p-4 text-white flex items-center space-x-2">
            <Image src={logo}
                   alt="logo" className="object-contain h-auto w-10 rounded-md"/>
            <h1 className="text-center text-xl font-bold text-white">Astudio</h1>

          </div>
          <hr className="border-1 border-white m-2"/>
        </div>

        {/* Content */}

        <div className="flex-1 p-4 bg-gray-200 flex flex-col justify-between">
          <div className="flex items-center space-x-2">
            <FaRobot className="text-indigo-500 mx-auto text-lg"/>
          </div>


          <div className="mt-4 p-4 bg-white rounded-lg shadow-md flex-grow">
            {/* chat messages */}
            <div className="flex-1 overflow-y-auto">
              {/* Messages will go here */}
            </div>
          </div>

          <div className="mt-4 p-4 bg-white rounded-lg shadow-md">
            {/* chat input box */}
            <div className="flex items-center space-x-2">
              <input type="text" className="flex-1 p-2 border border-gray-400 rounded"/>
              <button className="p-2 bg-indigo-500 text-white rounded flex items-center">
                <FaPaperPlane className="mr-2" /> Send
              </button>
            </div>
          </div>
        </div>
      </div>
    </div>
  );
}

