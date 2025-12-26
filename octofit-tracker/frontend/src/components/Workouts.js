import React, { useEffect, useState } from 'react';

const sampleWorkouts = [
  { name: 'Morning Run', type: 'Cardio', duration: '30 min' },
  { name: 'Yoga', type: 'Flexibility', duration: '45 min' }
];

const Workouts = () => {
  const [workouts, setWorkouts] = useState([]);
  const codespace = process.env.REACT_APP_CODESPACE_NAME;
  const endpoint = codespace
    ? `https://${codespace}-8000.app.github.dev/api/workouts/`
    : '/api/workouts/';

  useEffect(() => {
    fetch(endpoint)
      .then(res => res.json())
      .then(data => {
        const results = data.results || data;
        setWorkouts(results.length ? results : []);
      })
      .catch(() => setWorkouts([]));
  }, [endpoint]);

  const displayWorkouts = workouts.length ? workouts : sampleWorkouts;

  return (
    <div className="row justify-content-center">
      <div className="col-md-10">
        <div className="card shadow-sm mb-4">
          <div className="card-body">
            <h1 className="card-title display-6 mb-4 text-primary">Workouts</h1>
            <div className="table-responsive">
              <table className="table table-striped align-middle">
                <thead className="table-primary">
                  <tr>
                    <th scope="col">#</th>
                    <th scope="col">Workout Name</th>
                    <th scope="col">Type</th>
                    <th scope="col">Duration</th>
                    <th scope="col">Actions</th>
                  </tr>
                </thead>
                <tbody>
                  {displayWorkouts.map((workout, idx) => (
                    <tr key={idx}>
                      <th scope="row">{idx + 1}</th>
                      <td>{workout.name || workout.workout_name || 'N/A'}</td>
                      <td>{workout.type || workout.workout_type || 'N/A'}</td>
                      <td>{workout.duration || 'N/A'}</td>
                      <td>
                        <button className="btn btn-outline-primary btn-sm me-2">Edit</button>
                        <button className="btn btn-outline-danger btn-sm">Delete</button>
                      </td>
                    </tr>
                  ))}
                </tbody>
              </table>
            </div>
            <button className="btn btn-success mt-3">Add Workout</button>
          </div>
        </div>
      </div>
    </div>
  );
};

export default Workouts;
