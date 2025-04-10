"use client";

import React from "react";
import { Star } from "lucide-react";

const testimonials = [
  {
    name: "Dhairya",
    content: "Really liked the experience and would highly recommend!",
    rating: 5,
    categories: [1, 2],
  },
  {
    name: "Yash",
    content: "Great product and fantastic support!",
    rating: 4,
    categories: [1, 3],
  },
  {
    name: "Boba",
    content: "Very easy to use, and the team is super helpful.",
    rating: 3,
    categories: [1, 4],
  },
  {
    name: "Sarthak J",
    content: "A seamless experience from start to finish.",
    rating: 5,
    categories: [1, 5],
  },
  {
    name: "Neha",
    content: "Smooth workflow and beautiful design!",
    rating: 4,
    categories: [1, 4],
  },
  {
    name: "Arjun",
    content: "Decent experience but there's room for improvement.",
    rating: 2,
    categories: [1, 2],
  },
];

const categories = [
  { id: 1, label: "View All" },
  { id: 2, label: "User Experience" },
  { id: 3, label: "Performance" },
  { id: 4, label: "Design" },
  { id: 5, label: "Support" },
];

// ⭐ Read-only version
const StarRating = ({ rating }: { rating: number }) => (
  <div className="flex items-center gap-1">
    {Array.from({ length: 5 }, (_, i) => (
      <Star
        key={i}
        size={18}
        className={`stroke-yellow-400 ${i < rating ? "fill-yellow-400" : ""}`}
      />
    ))}
  </div>
);

export default function TestimonialSection() {
  const [category, setCategory] = React.useState(1);

  return (
    <section className="p-8 md:p-12 bg-gray-900 min-h-screen">
      <h2 className="text-3xl font-bold text-white mb-6">What People Say</h2>

      <div className="flex flex-wrap gap-3 mb-8">
        {categories.map((cat) => (
          <button
            key={cat.id}
            onClick={() => setCategory(cat.id)}
            className={`rounded-full border border-white px-4 py-2 text-sm ${category === cat.id
                ? "bg-white text-gray-900"
                : "bg-transparent text-white hover:bg-white/10"
              }`}
          >
            {cat.label}
          </button>
        ))}
      </div>

      <div className="grid grid-cols-1 sm:grid-cols-2 lg:grid-cols-3 gap-6">
        {testimonials
          .filter((t) => category === 1 || t.categories.includes(category))
          .map((t, index) => (
            <div
              key={index}
              className="bg-gray-800 p-6 rounded-2xl shadow-md transition-all duration-300 hover:scale-[1.02] text-white"
            >
              <div className="mb-4">
                <p className="text-lg font-semibold">{t.name}</p>
                <StarRating rating={t.rating} />
              </div>
              <p className="text-sm text-indigo-100/80">{t.content}</p>
            </div>
          ))}
      </div>
    </section>
  );
}



