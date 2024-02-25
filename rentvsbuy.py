import streamlit as st
import numpy as np


def generate_data(num_points, min_val, max_val):
  """Generates random data for the histogram."""
  return np.random.uniform(low=min_val, high=max_val, size=num_points)


def app():
  """Main function of the Streamlit app."""
  st.title("Histogram with Slider")

  # Define slider parameters
  num_points_min = 100
  num_points_max = 1000
  num_points_default = 500

  # Create slider
  num_points = st.slider(
      "Number of data points:",
      min_value=num_points_min,
      max_value=num_points_max,
      value=num_points_default,
  )

  # Generate data based on slider value
  data = generate_data(num_points, 0, 10)

  # Display histogram
  st.subheader("Histogram")
  st.bar_chart(data)


if __name__ == "__main__":
  app()
