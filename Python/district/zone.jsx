import React, { useState, useEffect } from 'react';
import axios from 'axios';

const ZoneForm = ({ onSubmit }) => {
  const [name, setName] = useState('');
  const [province, setProvince] = useState('');
  const [provinces, setProvinces] = useState([]);

  useEffect(() => {
    // Fetch provinces
    axios.get('/api/provinces')
      .then((response) => setProvinces(response.data))
      .catch((error) => console.error('Error fetching provinces:', error));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ name, province });
    setName(''); // Reset form
    setProvince(''); // Reset form
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="name">
          Zone Name
        </label>
        <input
          id="name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          placeholder="Enter zone name"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="province">
          Province
        </label>
        <select
          id="province"
          value={province}
          onChange={(e) => setProvince(e.target.value)}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          required
        >
          <option value="">Select a province</option>
          {provinces.map((province) => (
            <option key={province._id} value={province._id}>
              {province.name}
            </option>
          ))}
        </select>
      </div>
      <div className="flex items-center justify-between">
        <button
          type="submit"
          className="bg-blue-500 hover:bg-blue-700 text-white font-bold py-2 px-4 rounded focus:outline-none focus:shadow-outline"
        >
          Submit
        </button>
      </div>
    </form>
  );
};

export default ZoneForm;