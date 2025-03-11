import React, { useState, useEffect } from 'react';
import axios from 'axios';

const DistrictForm = ({ onSubmit }) => {
  const [name, setName] = useState('');
  const [zone, setZone] = useState('');
  const [zones, setZones] = useState([]);

  useEffect(() => {
    // Fetch zones
    axios.get('/api/zones')
      .then((response) => setZones(response.data))
      .catch((error) => console.error('Error fetching zones:', error));
  }, []);

  const handleSubmit = (e) => {
    e.preventDefault();
    onSubmit({ name, zone });
    setName(''); // Reset form
    setZone(''); // Reset form
  };

  return (
    <form onSubmit={handleSubmit} className="bg-white shadow-md rounded px-8 pt-6 pb-8 mb-4">
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="name">
          District Name
        </label>
        <input
          id="name"
          type="text"
          value={name}
          onChange={(e) => setName(e.target.value)}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          placeholder="Enter district name"
          required
        />
      </div>
      <div className="mb-4">
        <label className="block text-gray-700 text-sm font-bold mb-2" htmlFor="zone">
          Zone
        </label>
        <select
          id="zone"
          value={zone}
          onChange={(e) => setZone(e.target.value)}
          className="shadow appearance-none border rounded w-full py-2 px-3 text-gray-700 leading-tight focus:outline-none focus:shadow-outline"
          required
        >
          <option value="">Select a zone</option>
          {zones.map((zone) => (
            <option key={zone._id} value={zone._id}>
              {zone.name}
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

export default DistrictForm;