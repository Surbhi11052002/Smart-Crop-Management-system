import React from "react";
import preLogo from "../img/preHeaderLogo.png";
import "./preheader.css";

const PreHeader = () => {
  return (
    <div className="bg-[rgb(128,150,33)] px-6 py-2 md:inline-block hidden w-full">
      <div className="flex justify-between items-center ml-6">
        <div className="flex justify-center items-center">
          <img src={preLogo} className="logo" alt="PreHeader Logo" />
          <p className="font-semibold text-white text-xs sm:text-sm ml-1">
            Harvesting Solutions: Join Our Farmers’ Aid Hub!
          </p>
        </div>
        <div className="">
          <div className="" id="google_element"></div>
        </div>
      </div>
    </div>
  );
};

export default PreHeader;
