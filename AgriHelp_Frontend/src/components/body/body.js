import "../../index.css";
import "./body.css";

const Body = () => {
  return (
    <div className="body">
      <div className="background-image grid place-items-center my-6 text-center">
        <div className="">
          <p className="text-3xl  font-bold  text-white uppercase mb-4 mr-20">
            Farmers’ Aid Hub
          </p>
          <p className="text-6xl font-medium  text-lime-600 max-w-md mb-4">
            AGRI HELP
          </p>
          <p className="text-2xl font-bold  text-white">
            Harvesting Innovation, Nurturing Possibilities.
          </p>
        </div>
      </div>
      {/* <CardBar />
      <HelpCard />
      <section className="flex flex-col py-5">
        <div className="grid place-items-center my-14 ">
          <p className="text-3xl font-bold text-center text-gray-900 uppercase mb-2">
            FEATURES EXPLORED
          </p>
          <p className="text-xl font-medium text-center text-gray-500 max-w-md">
            {" "}
            Take a look at our features
          </p>
        </div>
        <img src={FeatureImg} alt="features"></img>
      </section> */}
    </div>
  );
};

export default Body;
