# Pipe Fitting And Accessory Pressure Drop Item Class

Source: https://www.revitapidocs.com/2026/5fb04b00-61d7-d8d6-cf12-e30ad04ea3e7.htm

---

| Pipe Fitting And Accessory Pressure Drop Item Class |
| --- |

A flow path of the pipe/pipe fitting and accessory. It is defined by the begin connector and end connector ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Plumbing PipeFittingAndAccessoryPressureDropItem 
  
**Namespace:** [Autodesk.Revit.DB.Plumbing](cc553597-37c2-fcd9-6025-d904c129c80a.htm) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class PipeFittingAndAccessoryPressureDropItem : IDisposable
```

```
Public Class PipeFittingAndAccessoryPressureDropItem
	Implements IDisposable
```

```
public ref class PipeFittingAndAccessoryPressureDropItem : IDisposable
```

```
type PipeFittingAndAccessoryPressureDropItem = 
    class
        interface IDisposable
    end
```
The PipeFittingAndAccessoryPressureDropItem type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [BeginConnectorIndex](Pipe-Fitting-And-Accessory-Pressure-Drop-Item-Begin-Connector-Index-Property.md) | The index of the begin connector of the flow path. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Coefficient](Pipe-Fitting-And-Accessory-Pressure-Drop-Item-Coefficient-Property.md) | The coefficient between the begin connector and end connector, unitlesss. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [EndConnectorIndex](Pipe-Fitting-And-Accessory-Pressure-Drop-Item-End-Connector-Index-Property.md) | The index of the end conector of the flow path. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](b0eb1097-de50-b1b7-5e6e-274fdfa4b163.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [VelocityPressure](95df69a8-1347-e254-fc16-6a64f427b816.htm) | The velocity pressure, for converting between coefficient and pressure drop on this flow path. Units: (kg/(ftÂ·sÂ²)). |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](f8904fba-6518-b346-51c3-03be73bbaac7.htm) | Releases all resources used by the PipeFittingAndAccessoryPressureDropItem |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Plumbing Namespace](cc553597-37c2-fcd9-6025-d904c129c80a.htm)
