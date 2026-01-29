
import React from 'react';
import styles from './ComparisonView.module.css';

const ComparisonView = ({ products }) => {
    if (!products || products.length === 0) return null;

    const features = [
        { label: 'Price', key: 'price', format: (v) => `₹${v.toLocaleString('en-IN')}` },
        { label: 'Display', key: 'specs.display' },
        { label: 'Processor', key: 'specs.processor' },
        { label: 'RAM', key: 'specs.ram' },
        { label: 'Storage', key: 'specs.storage' },
        { label: 'Camera', key: 'specs.camera' },
        { label: 'Battery', key: 'specs.battery' },
    ];

    const getValue = (obj, path) => {
        return path.split('.').reduce((o, k) => (o || {})[k], obj);
    };

    return (
        <div className={styles.container}>
            <table className={styles.table}>
                <thead>
                    <tr>
                        <th className={styles.th}>Feature</th>
                        {products.map(p => (
                            <th key={p.id} className={styles.thProduct}>{p.name}</th>
                        ))}
                    </tr>
                </thead>
                <tbody>
                    {features.map((feature) => (
                        <tr key={feature.label}>
                            <td className={styles.tdLabel}>{feature.label}</td>
                            {products.map(p => (
                                <td key={p.id} className={styles.td}>
                                    {feature.format ? feature.format(getValue(p, feature.key)) : getValue(p, feature.key)}
                                </td>
                            ))}
                        </tr>
                    ))}
                </tbody>
            </table>
        </div>
    );
};

export default ComparisonView;
