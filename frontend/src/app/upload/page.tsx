'use client';
import React, {useState} from "react";
import {baseUrl} from "../../config";
import Link from "next/link";

export default function Page() {
  const [success, setSuccess] = useState(false);
  const [error, setError] = useState(false);
  const [file, setFile] = useState(null);


  const handleUpload = (e: any) => {
    e.preventDefault();
    const file = e.target.files[0];
    const formData = new FormData();
    const timeNow = new Date().getTime();
    formData.append("file", file);
    formData.append("title", "CV"+timeNow);

    fetch(baseUrl+"api/data/documents/", {
      method: "POST",
      body: formData,
    })
      .then((response) => response.json())
      .then((data) => {
        console.log(data);
        setSuccess(true);
      }).catch((error) => {
        console.error("Error:", error);
        setError(true);
    });
  };

  return (
    <>
      {success && (
        <div className="bg-green-200 border-l-4 border-green-500 text-green-700 p-4" role="alert">
          <p className="font-bold">Success</p>
          <p>File uploaded successfully</p>
        </div>
      )}
      {error && (
        <div className="bg-red-200 border-l-4 border-red-500 text-red-700 p-4" role="alert">
          <p className="font-bold">Error</p>
          <p>There was an error uploading the file</p>
        </div>
      )}


      <div className="flex flex-col items-center justify-center
                      justify-center bg-gray-800 h-screen items-center">
        <div className="flex flex-col items-center justify-center min-h-screen">
          <div className="w-auto h-auto bg-gray-800">
            <h1 className="text-4xl text-white font-bold text-center">Upload your CV</h1>
            <hr className="border-1 border-black m-2" />
          </div>
          <div className="flex w-64 h-auto bg-gray-800 p-4">
            <input
              type="file"
              onChange={handleUpload}
              className="block w-full text-sm text-gray-500 file:mr-4 file:py-2 file:px-4 file:rounded-full file:border-0 file:text-sm file:font-semibold file:bg-blue-50 file:text-blue-700 hover:file:bg-blue-100"
            />
          </div>



        </div>
      </div>

    </>
  );
}
