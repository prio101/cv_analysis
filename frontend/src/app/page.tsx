import Link from 'next/link';

export default function Page() {
  return (
    <div className="container mx-auto items-center justify-center
                    bg-gray-800 h-screen items-center justify-center">
      <div className="flex flex-col items-center justify-center h-full w-full">
        <div className='w-64 h-auto bg-gray-800'>
          <h1 className="text-4xl text-white font-bold text-center">Welcome to Astudio</h1>
          <hr className="border-1 border-black m-2"/>
        </div>
      </div>
    </div>
  );
}
