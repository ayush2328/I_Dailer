'use client';
import { useState } from 'react';
import { Star } from 'lucide-react';
import clsx from 'clsx';

interface StarRatingProps {
    totalStars?: number;
    onRate?: (rating: number) => void;
    defaultRating?: number;
}

export default function StarRating({
    totalStars = 5,
    onRate,
    defaultRating = 0,
}: StarRatingProps) {
    const [rating, setRating] = useState(defaultRating);
    const [hover, setHover] = useState<number | null>(null);

    const handleClick = (index: number) => {
        setRating(index);
        onRate?.(index);
    };

    return (
        <div className="flex gap-1">
            {Array.from({ length: totalStars }, (_, i) => i + 1).map((star) => (
                <Star
                    key={star}
                    size={24}
                    className={clsx(
                        'cursor-pointer transition-colors',
                        (hover ?? rating) >= star ? 'text-yellow-400' : 'text-gray-300'
                    )}
                    onMouseEnter={() => setHover(star)}
                    onMouseLeave={() => setHover(null)}
                    onClick={() => handleClick(star)}
                    fill={(hover ?? rating) >= star ? '#facc15' : 'none'}
                />
            ))}
        </div>
    );
}
