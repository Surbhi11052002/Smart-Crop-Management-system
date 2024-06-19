import React, { useEffect } from "react";
import "./footer.css";
import { useNavigate, useLocation } from "react-router-dom";
import logo from "../img/main_logo.png";
import Vector from "../img/Vector.png";
import Vector1 from "../img/Vector1.png";
import Vector2 from "../img/Vector2.png";

const Footer = () => {
  const navigate = useNavigate();
  const location = useLocation();

  useEffect(() => {
    window.scrollTo(0, 0);
  }, [location.pathname]);

  return (
    <div className="bg-[#739621] inPhone py-20">
      <div className="flex justify-center items-center">
        <div className="flex-1 border-r-2 border-black-600">
          <div
            className="flex justify-center items-center mx-8 cursor-pointer"
            onClick={() => navigate("/")}
          >
            <img src={logo} className="footerLogo" alt="" />
            <div className="ml-4">
              <h3 className="text-2xl text-white font-bold mt-4">Agri Help</h3>
              <p className="text-md font-normal text-white mt-2">
                Harvesting Innovation, Nurturing Possibilities.
              </p>
            </div>
          </div>
        </div>
        <div className="flex-1 px-16 border-r-2 border-black-600">
          <div className="flex">
            <ul className="list-none mr-24">
              <li
                className="text-lg text-white font-medium cursor-pointer"
                onClick={() => navigate("/")}
              >
                Home
              </li>
            </ul>
            <ul>
              <li
                className="text-lg text-white font-medium cursor-pointer"
                onClick={() => navigate("/fertilizer")}
              >
                Fertilizer Prediction
              </li>
              <li
                className="text-lg text-white font-medium cursor-pointer"
                onClick={() => navigate("/crop")}
              >
                Crop Prediction
              </li>

              <li
                className="text-lg text-white font-medium cursor-pointer"
                onClick={() => navigate("/disease")}
              >
                Disease Prediction
              </li>
            </ul>
          </div>
        </div>
        <div className="flex-1 px-16 border-r-2 border-black-600">
          <h1 className="text-xl ml-6 text-white font-bold w-2/3">
            Give us a follow on social media
          </h1>
          <div className="flex my-5 justify-left">
            <img
              className="socialIcons mx-3 ml-6 cursor-pointer"
              src={Vector}
              alt=""
            />
            <img
              className="socialIcons mx-3 ml-6 cursor-pointer"
              src={Vector1}
              alt=""
            />
            <img
              className="socialIcons mx-3 ml-6 cursor-pointer"
              src={Vector2}
              alt=""
            />
          </div>
        </div>
      </div>
    </div>
  );
};

export default Footer;
