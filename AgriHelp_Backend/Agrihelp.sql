

SET SQL_MODE = "NO_AUTO_VALUE_ON_ZERO";
START TRANSACTION;
SET time_zone = "+00:00";


/*!40101 SET @OLD_CHARACTER_SET_CLIENT=@@CHARACTER_SET_CLIENT */;
/*!40101 SET @OLD_CHARACTER_SET_RESULTS=@@CHARACTER_SET_RESULTS */;
/*!40101 SET @OLD_COLLATION_CONNECTION=@@COLLATION_CONNECTION */;
/*!40101 SET NAMES utf8mb4 */;

--
-- Base de datos: `geeks_on_fire`
--

-- --------------------------------------------------------

--
-- Estructura de tabla para la tabla `topics`
--

CREATE TABLE `topics` (
  `id` int(11) NOT NULL,
  `topic_title` varchar(30) NOT NULL,
  `content` varchar(120) NOT NULL
) ENGINE=InnoDB DEFAULT CHARSET=utf8mb4;

--
-- Volcado de datos para la tabla `topics`
--

INSERT INTO `topics` (`id`, `topic_title`, `content`) VALUES
(1, 'fertilizers', 'Fertilizers are a susbstances rich in nutients that are to improve the characteristics of the soil for a greater develop'),
(2, 'cultivation', 'Cultivation is the action of working the land depending on whether there are and grow plant species.'),
(3, 'nutrition', 'Nutrition is the biological progress in which animal and plant organisms absorb the nutrients necessary for life from fo'),
(4, 'harvest', 'Harvest is the set of fruits that are collected from the groud at the time year they are ripe.');

--
-- Índices para tablas volcadas
--

--
-- Indices de la tabla `topics`
--
ALTER TABLE `topics`
  ADD PRIMARY KEY (`id`);

--
ALTER TABLE `topics`
  MODIFY `id` int(11) NOT NULL AUTO_INCREMENT, AUTO_INCREMENT=5;
COMMIT;

