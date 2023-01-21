import React from "react";
import { Route, Navigate ,Outlet} from "react-router-dom";

// const ProtectedRoute = ({ auth, component: Component, ...rest }) => {
//   return (
//     <Route
//       {...rest}
//       render={(props) => {
//         if (auth)
//        {  return <Component {...props} />;}
//         else{
//           return (
//             <Navigate to={{ path: "/", state: { from: props.location } }} />
//           );
//         }
//       }}
//     />
//   );
// };

const ProtectedRoute = ({ auth, children }) => {
    console.log(auth)
    if (auth) {
        return children;
     
    }
  
    return <Navigate to="/login" replace />;
  };
  // const ProtectedRoute = ({ auth}) => {
  //   console.log(auth)
  //   if (auth) {
  //       return <Outlet/>;
     
  //   }
  
  //   return <Navigate to="/login" replace />;
  // };

export default ProtectedRoute;