# Analytical Transformer Data Class

Source: https://www.revitapidocs.com/2026/a4235b4c-ad58-bb3f-e697-2e7ba5bef5ea.htm

---

| Analytical Transformer Data Class |
| --- |

Represents the data and parameters of analytical transformer node. ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Inheritance Hierarchy System Object 
[Autodesk.Revit.DB.Electrical AnalyticalDistributionNodePropertyData](Analytical-Distribution-Node-Property-Data-Class.md) 
[Autodesk.Revit.DB.Electrical AnalyticalPowerDistributableNodeData](Analytical-Power-Distributable-Node-Data-Class.md) 
Autodesk.Revit.DB.Electrical AnalyticalTransformerData 
  
**Namespace:** [Autodesk.Revit.DB.Electrical](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md) 
**Assembly:** RevitAPI (in RevitAPI.dll) Version: 26\.0\.4\.0 (26\.0\.4\.0\) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Syntax [C\#](#) [VB](#) [C\+\+](#) [F\#](#) 
```
public class AnalyticalTransformerData : AnalyticalPowerDistributableNodeData
```

```
Public Class AnalyticalTransformerData
	Inherits AnalyticalPowerDistributableNodeData
```

```
public ref class AnalyticalTransformerData : public AnalyticalPowerDistributableNodeData
```

```
type AnalyticalTransformerData = 
    class
        inherit AnalyticalPowerDistributableNodeData
    end
```
The AnalyticalTransformerData type exposes the following members. 

![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Properties 

|  | Name | Description |
| --- | --- | --- |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ApparentPowerRating](d7965632-fd13-476c-5a38-5bf3a6ac8e51.htm) | The apparent power rating value of the analytical transformer. |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AssignedPhasesNumber](9d6d49c1-91b4-8ef4-26c0-b044938d2824.htm) | The number of electrical phases assigned through the distribution system of the power distributable node. (Inherited from [AnalyticalPowerDistributableNodeData](Analytical-Power-Distributable-Node-Data-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [AssignedVoltage](10ee95c6-68b3-5fc0-6219-573180244db9.htm) | The voltage assigned through the distribution system of the power distributable node. (Inherited from [AnalyticalPowerDistributableNodeData](Analytical-Power-Distributable-Node-Data-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [ConnectedPhases](bcb78144-2b99-cb70-7172-bfca78e2c27c.htm) | The electrical connected phases of the electrical analytical node to its upstream node. (Inherited from [AnalyticalDistributionNodePropertyData](Analytical-Distribution-Node-Property-Data-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [DistributionSystem](a271a35f-d65a-b22e-9579-c3038854f0bb.htm) | The distribution system of the power distributable node. (Inherited from [AnalyticalPowerDistributableNodeData](Analytical-Power-Distributable-Node-Data-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [IsValidObject](d3767f0c-ecb2-e6bc-3b6f-0a65f71204b2.htm) | Specifies whether the .NET object represents a valid Revit entity. (Inherited from [AnalyticalDistributionNodePropertyData](Analytical-Distribution-Node-Property-Data-Class.md) ) |
| ![Public property](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubproperty.gif "Public property") | [SecondaryDistributionSystem](df6261db-4ad4-7d00-9fd2-d3ebdc988351.htm) | The secondary distribution system of the analytical transformer. |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)Methods 

|  | Name | Description |
| --- | --- | --- |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [Dispose](f7dfe5ca-7afd-202a-cce0-8d4e0ce3a8fb.htm) | (Inherited from [AnalyticalDistributionNodePropertyData](Analytical-Distribution-Node-Property-Data-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | Equals | Determines whether the specified object is equal to the current object. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetAllAvailableConnectedPhasesOnDownstream](3937cb9b-34c1-9f9f-7043-309ace9887ec.htm) | Get all the available electrical connected phases that this power distributable node can provide to the downstream node. (Inherited from [AnalyticalPowerDistributableNodeData](Analytical-Power-Distributable-Node-Data-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetApparentPerPhaseResults](2cdf8943-793a-1fcb-880a-c2dbd303012b.htm) | Get an ElectricalPerPhaseData which contains each electrical phase's apparent load and apprent current of the power distributable node. (Inherited from [AnalyticalPowerDistributableNodeData](Analytical-Power-Distributable-Node-Data-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetConnectedPhasesOnDownstream](def48076-10be-2d07-29f1-d5eb02f46f94.htm) | Get the electrical connected phases of the downstream node. (Inherited from [AnalyticalPowerDistributableNodeData](Analytical-Power-Distributable-Node-Data-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [GetDemandPerPhaseResults](039649ce-c681-a1a2-569f-c6facd2245de.htm) | Get an ElectricalPerPhaseData which contains each electrical phase's demand load and demand current of the power distributable node. (Inherited from [AnalyticalPowerDistributableNodeData](Analytical-Power-Distributable-Node-Data-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetHashCode | Serves as the default hash function. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | GetType | Gets the Type of the current instance. (Inherited from Object ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | [SetConnectedPhasesOnDownstream](2e8c09ca-d8b6-d586-a8b0-b221d84ef593.htm) | Set the electrical connected phases of the downstream node. (Inherited from [AnalyticalPowerDistributableNodeData](Analytical-Power-Distributable-Node-Data-Class.md) ) |
| ![Public method](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/pubmethod.gif "Public method") | ToString | Returns a string that represents the current object. (Inherited from Object ) |

[Top](#PageHeader) ![](https://d24b2zsrnzhmgb.cloudfront.net/static/img/chm/icons/sectionexpanded.png)See Also 

#### Reference

[Autodesk.Revit.DB.Electrical Namespace](../ungrouped/Autodesk.-Revit.-DB.-Electrical-Namespace.md)
