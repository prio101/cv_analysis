'use client'
import React, {useState, useEffect} from "react";
import Image from "next/image";
import logo from "/public/logo.png";
import { FaPaperPlane, FaRobot, FaCogs, FaClock } from "react-icons/fa"; // Import an icon from React Icons
import { baseUrl } from "@/config";

export default function Page() {
  const [replies, setReplies] = useState<string[][]>([]);
  const [questions, setQuestions] = useState<string[][]>([]);
  const [messages, setMessages] = useState<string[][]>([]);
  const [startSession, setStartSession] = useState(false);
  const [sessionId, setSessionId] = useState("");
  const [process, setProcess] = useState(false);

  useEffect(() => {

  }, [replies]);

  const handleRagPreProcess = async () => {
    const response = await fetch(baseUrl+"/api/rag/run_rag", {
      method: "GET",
      headers: {
        "Content-Type": "application/json",
      }
    });

    // If the request was successful, log the response
    if (response.ok) {
      setProcess(true);
      setTimeout(() => {
        setProcess(false);
      }, 5000);
      console.log(await response.json());
    }
  };

  const handleSession = async () => {
    const response = await fetch(baseUrl+"/api/chat/start-session/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      }
    });

    // If the request was successful, log the response
    if (response.ok) {
      setStartSession(true);
      const data = await response.json();
      setSessionId(data.chat_session_id);
    } else {
      console.error("Failed to start session");
    }
  };

  const handleChat = async () => {
    const body = {
      chat_session_id: sessionId,
      query: messages[messages.length - 1],
    }
    console.log(body);

    const response = await fetch(baseUrl+"/api/chat/message/", {
      method: "POST",
      headers: {
        "Content-Type": "application/json",
      },
      body: JSON.stringify(body),
    });

    // If the request was successful, log the response
    if (response.ok) {
      const data = await response.json();
      setReplies([...replies, [data.response]]);
      setQuestions([...questions, body.query]);
      // clear the input box only
      const inputElement = document.getElementById("chatInput") as HTMLInputElement;
      if (inputElement) {
        inputElement.value = '';
      }
    } else {
      console.error("Failed to send message");
    }
  };

  return (
    <div className="container bg-gray-800 h-screen">
      <div className="flex flex-col md:flex-row bg-gray-800 h-screen">
        {/* Sidebar */}
        <div className="w-64 h-auto bg-gray-800 ">
          <div className="p-4 text-white flex items-center space-x-2">
            <Image src={logo}
                   alt="logo" className="object-contain h-auto w-10 rounded-md"/>
            <h1 className="text-center text-xl font-bold text-white">Astudio</h1>

          </div>
          <hr className="border-1 border-white m-2"/>
          <div className="p-4 text-white items-center space-x-2 flex flex-col">
            <button onClick={handleRagPreProcess} className="p-2 cursor-pointer bg-indigo-500
                                                             text-white
                                                             rounded flex items-center">
              <FaCogs className="mr-2" />
              Run Rag
            </button>
            <span className="py-2 text-white text-xs">For Newly Collected CVs Run this before start chatting.
              You are in control
            </span>
            {process && (
              <>
                <FaClock className="mr-2 text-xl animate-pulse text-purple-200"  />
                <span className="py-2 text-white text-xs text-center rounded-full my-4 w-full">
                  Processing...
                </span>
              </>

            )}
          </div>
        </div>

        {/* Content */}

        <div className="flex-1 p-4 bg-gray-200 flex flex-col justify-between">
          <div className="flex items-center space-x-2">
            <FaRobot className="text-indigo-500 mx-auto text-lg"/>
          </div>

          {startSession  && (
            <>
              <div className="mt-4 p-4 bg-white rounded-lg shadow-md flex-grow">
                {/* chat messages */}
                <div className="flex-1 flex-col h-full overflow-y-auto scrollbar">
                  {replies.map((reply, index) => (
                  <div key={index} className="flex flex-col space-x-2">
                    <div className="my-2 w-auto p-2 bg-gray-900 text-white rounded text-end">
                    {questions[index]}
                    <span className="text-xs text-gray-400"> - You</span>
                    </div>

                      {reply && (
                        <div className="my-2 w-auto p-2 bg-indigo-500 text-white rounded text-start">
                          {reply}
                          <span className="text-xs text-gray-400"> - Astudio Bot</span>
                        </div>
                      )}
                  </div>
                  ))}
                </div>
              </div>
              <div className="mt-4 p-4 bg-white rounded-lg shadow-md">
                {/* chat input box */}
                <div className="flex items-center space-x-2">
                  <input id="chatInput" type="text" onChange={e => setMessages([e.target.value])} className="flex-1 p-2 border border-gray-400 rounded"/>
                  <button
                    onKeyDown={e => e.key === 'Enter' && handleChat()}
                    onClick={handleChat} className="cursor-pointer p-2 bg-indigo-500 text-white rounded flex items-center">
                    <FaPaperPlane className="mr-2" /> Send
                  </button>
                </div>
              </div>
            </>
          )}

          {!startSession && (
            <div className="mt-4 p-4 bg-white rounded-lg shadow-md flex flex-col items-center justify-center">
              <div className="flex items-center space-x-2">
                <button onClick={handleSession} className=" cursor-pointer p-2 bg-indigo-500 text-white rounded flex items-center">
                  <FaRobot className="mr-2" /> Start Chat
                </button>
              </div>
            </div>
          )}

        </div>
      </div>
    </div>
  );
}

