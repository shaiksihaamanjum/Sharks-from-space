class SharkTrackingPipeline:
    def __init__(self, model_path=None, api_keys=None):
        # Dummy model attributes for health check and info endpoint
        self.detection_model = type('DummyModel', (), {
            'img_size': (224, 224),
            'confidence_threshold': 0.5
        })()
        self.model_path = model_path
        self.api_keys = api_keys

    def process_satellite_image(self, image_array, latitude, longitude):
        # Dummy implementation: always returns a fake detection
        return {
            "detections": [
                {
                    "species": "Great White",
                    "confidence": 0.95,
                    "location": {
                        "latitude": latitude,
                        "longitude": longitude
                    }
                }
            ],
            "input_shape": str(getattr(image_array, "shape", "unknown"))
        }

    class data_processor:
        @staticmethod
        def get_environmental_data(latitude, longitude):
            # Dummy environmental data
            return {
                "temperature": 24.5,
                "salinity": 35.1,
                "chlorophyll": 0.8,
                "latitude": latitude,
                "longitude": longitude
            }