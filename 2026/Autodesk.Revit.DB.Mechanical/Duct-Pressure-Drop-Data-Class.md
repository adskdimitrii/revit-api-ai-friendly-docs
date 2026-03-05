# Duct Pressure Drop Data Class

Source: https://www.revitapidocs.com/2026/53565301-b25a-cd38-0c68-bed19d619c25.htm

---

| Duct Pressure Drop Data Class |
| --- |

The input and output data used by external servers for calculation of the duct pressure drop. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Mechanical DuctPressureDropData 
  
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class DuctPressureDropData : IDisposable
```

```
Public Class DuctPressureDropData
	Implements IDisposable
```

```
public ref class DuctPressureDropData : IDisposable
```

```
type DuctPressureDropData = 
    class
        interface IDisposable
    end
```
The DuctPressureDropData type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [CategoryId](facb8291-71f9-a9b5-4abf-6389a5401136.htm) | The category id of duct curves. It will be OST\_DuctCurves, OST\_FlexDuctCurves, or OST\_PlaceHolderDucts. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Coefficient](30c73e0a-612a-d09a-26f9-6a58d5d1378b.htm) | The coefficient of the duct. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Density](48c06939-e1fc-3160-3302-d1830041098a.htm) | The density of the duct. Units: (kg/ftÂ³). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DynamicViscosity](8222750c-a7cd-e833-0ba2-ac31a0273fd7.htm) | The dynamic viscosity of the air in the duct. Units: (kg/(ft\*s)). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Flow](51942eb2-777f-1a16-5406-bc2320827d21.htm) | The flow of the duct. Units: (ftÂ³/s). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Friction](628746d9-b8fa-a89e-21e9-97085309122d.htm) | The friction of the duct. Units: (kg/(ftÂ²Â·sÂ²)). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Height](7e160200-8c3f-a5d3-37ab-283cb21ee004.htm) | The height of the duct. If the duct is round, it will be equal to the diameter of the duct. Units: (ft). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [HydraulicDiameter](bcb8a3ff-b181-d37b-c165-b36cb9fad32e.htm) | The hydraulic diameter of the duct. Units: (ft). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](8f1feb00-c38f-1462-fb57-5c8c345e9d38.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Length](6ed4c1fd-b680-dc3a-1764-d95819ba5f0e.htm) | The length of the duct. Units: (ft). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Level](4c461eeb-7be6-86a9-d81d-9f35873c0a78.htm) | The calculation level of the system. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [PressureDrop](95dae130-a635-c9ff-07c9-7ecd24cbcefd.htm) | The pressure drop of the duct. Units: (kg/(ftÂ·sÂ²)). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ReynoldsNumber](15aa8a7d-a2ba-40e5-2ec6-97a0e70a163a.htm) | The reynolds number of the duct. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Roughness](e7047478-45b1-a611-86da-3e1e2b214870.htm) | The roughness of the duct. Units: (ft). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Shape](d63c2f48-c74c-bb2c-4f48-f3577fbb8684.htm) | The profile type of the duct. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Velocity](ed2a2ffa-bf61-7312-1d7b-def50b5ecbed.htm) | The velocity of the duct. Units: (ft/s). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [VelocityPressure](8a9a9aa8-000c-a7f3-99f8-56a058a7a77d.htm) | The velocity pressure of the duct. Units: (kg/(ftÂ·sÂ²)). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [WidthOrDiameter](518560a8-999c-86f7-9e19-e78030b7822c.htm) | The diameter of the duct with round profile, or the width of the duct with other profiles. Units: (ft). |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](7915f167-a6ea-659d-ced8-fecb38f5a5f1.htm) | Releases all resources used by the DuctPressureDropData |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks Profile type, Height, Diameter for round profile or width for other profiles, Length, Density, Viscosity, Roughness and Flow are input field values for the calculation. HydraulicDiameter, ReynoldsNumber, Velocity, VelocityPressure, Friction, PressureDrop, and Coefficient are output field values for the calculation ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
