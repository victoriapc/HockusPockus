from VisionPuckDetector.PuckDetectorBuilder import PuckDetectorBuilder

if __name__ == "__main__" :
    MODE = PuckDetectorBuilder.USB
    builder = PuckDetectorBuilder(MODE,30)
    pd = builder.build()
    pd.findPuck()
