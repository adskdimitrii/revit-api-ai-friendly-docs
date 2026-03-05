# Duct Fitting And Accessory Pressure Drop Item Class

Source: https://www.revitapidocs.com/2026/edcbddd9-85e5-a74d-7f1a-a9e28c1b4164.htm

---

| Duct Fitting And Accessory Pressure Drop Item Class |
| --- |

A flow path of the duct/pipe fitting and accessory. It is defined by the begin connector and end connector. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Mechanical DuctFittingAndAccessoryPressureDropItem 
  
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class DuctFittingAndAccessoryPressureDropItem : IDisposable
```

```
Public Class DuctFittingAndAccessoryPressureDropItem
	Implements IDisposable
```

```
public ref class DuctFittingAndAccessoryPressureDropItem : IDisposable
```

```
type DuctFittingAndAccessoryPressureDropItem = 
    class
        interface IDisposable
    end
```
The DuctFittingAndAccessoryPressureDropItem type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BeginConnectorIndex](c27909da-bb93-2983-df7c-4121061d7143.htm) | The index of the begin connector of the flow path. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Coefficient](Duct-Fitting-And-Accessory-Pressure-Drop-Item-Coefficient-Property.md) | The coefficient between the begin connector and end connector, unitless. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [EndConnectorIndex](dd4f9ccb-412d-d4fc-cf1b-709c7c2e8493.htm) | The index of the end conector of the flow path. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](641a6b90-4dfa-0f03-009e-17db7a734e7f.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [VelocityPressure](116033d9-b0dd-13e4-d22f-80f5b9f90e15.htm) | The velocity pressure, for converting between coefficient and pressure drop on this flow path. Units: (kg/(ftÂ·sÂ²)). |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](f04e4d12-a13b-8c66-824e-56240c24075d.htm) | Releases all resources used by the DuctFittingAndAccessoryPressureDropItem |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
