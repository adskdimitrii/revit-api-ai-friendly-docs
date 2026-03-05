# Duct Fitting And Accessory Data Class

Source: https://www.revitapidocs.com/2026/7db20bd9-6fba-bbd3-96ce-d08c0eec66c0.htm

---

| Duct Fitting And Accessory Data Class |
| --- |

The input data used by external servers for calculation of the duct fitting and duct accessory coefficient. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
Autodesk.Revit.DB.Mechanical DuctFittingAndAccessoryData 
  
**Namespace:** [Autodesk.Revit.DB.Mechanical](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class DuctFittingAndAccessoryData : IDisposable
```

```
Public Class DuctFittingAndAccessoryData
	Implements IDisposable
```

```
public ref class DuctFittingAndAccessoryData : IDisposable
```

```
type DuctFittingAndAccessoryData = 
    class
        interface IDisposable
    end
```
The DuctFittingAndAccessoryData type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Density](Duct-Fitting-And-Accessory-Data-Density-Property.md) | The air density for the duct fitting or duct accessory, Units: kg/ft^3\. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DynamicViscosity](Duct-Fitting-And-Accessory-Data-Dynamic-Viscosity-Property.md) | The dynamic viscosity of air for the duct fitting or duct accessory, Units: (kg/(ftÂ·s)). |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](fd6dd959-097d-38ce-2ce4-7295cb9f03bb.htm) | Specifies whether the .NET object represents a valid Revit entity. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [Origin](e861b86d-b8ef-6978-3c78-1ff297e512ff.htm) | The origin position of the duct fitting or duct accessory. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [PartType](798cb715-a76a-1a2e-7162-abba4f773337.htm) | The part type of the duct fitting or duct accessory. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ServerGUID](94277b06-9ddc-a15a-032e-984176ddbd44.htm) | The GUID of the duct fitting or duct accessory. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SystemClassification](b6c60ee8-b012-b506-dc42-a47c82ee9e7c.htm) | The system classification of the duct fitting or duct accessory. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](a637738b-5a16-7783-de47-0829610e360d.htm) | Releases all resources used by the DuctFittingAndAccessoryData |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetAllConnectorData](6a6fd6cc-325d-4d44-6e08-309cdc81ef42.htm) | Gets the connector data of the pipe fitting or pipe accessory. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetEntity](c1e1344a-74d7-fd84-877f-e4513270e61c.htm) | Returns an Entity of the Schema of the serverGUID.  or an invalid entity otherwise. |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetFamilyInstanceId](b219f66a-497c-b7ca-a1fa-6cf36287b7a4.htm) | Gets the Id of the fiting or accessory instance |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Remarks A FamilyInstance is the input data for the calculation, ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Mechanical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Mechanical-Namespace.md)
