
import React from 'react';
import styles from './ProductCard.module.css';

const ProductCard = ({ product, onSelect }) => {
    return (
        <div className={styles.card}>
            <div className={styles.imagePlaceholder}>
                <span className={styles.brand}>{product.brand}</span>
            </div>
            <div className={styles.content}>
                <h3 className={styles.name}>{product.name}</h3>
                <p className={styles.price}>₹{product.price.toLocaleString('en-IN')}</p>
                <div className={styles.specs}>
                    <span>{product.specs.display.split(',')[0]}</span>
                    <span>{product.specs.processor}</span>
                </div>
                <button
                    className={styles.button}
                    onClick={() => onSelect(product)}
                >
                    View Details
                </button>
            </div>
        </div>
    );
};

export default ProductCard;
