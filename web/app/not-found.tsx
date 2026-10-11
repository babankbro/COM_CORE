import Link from "next/link";

export default function NotFound() {
  return (
    <div className="max-w-2xl mx-auto px-6 py-24 text-center">
      <p className="text-6xl font-bold text-gray-300 dark:text-gray-700 mb-4">404</p>
      <h1 className="text-xl font-semibold text-gray-900 dark:text-white mb-2">ไม่พบหน้าที่ต้องการ</h1>
      <p className="text-gray-500 dark:text-gray-400 mb-6">หน้านี้อาจถูกย้ายหรือยังไม่มีเนื้อหา</p>
      <Link href="/" className="inline-flex px-4 py-2 rounded-lg bg-blue-600 text-white font-medium hover:bg-blue-700 transition-colors">
        กลับหน้าหลัก
      </Link>
    </div>
  );
}
